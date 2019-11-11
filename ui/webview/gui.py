#!/usr/bin/python3
# -*- coding: UTF-8 -*-

#from gui import internationalization

from flask import Flask
#import flask
from ui.webview.controllers.routes import flaskRoutes

#from flask_restful import Resource, Api

#from ui.webview import app 

import webview
import sys
import threading

#app = Flask(__name__)
#app.register_blueprint(flaskRoutes)

#api = Api(app)

#server.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1  # disable caching


#@app.after_request
#def add_header(response):
#    response.headers['Cache-Control'] = 'no-store'
#    return response

class Gui(Flask):
    def __init__(self, import_name=__name__, core=None, db=None):
        super(Gui, self).__init__(import_name=__name__, static_folder='static', template_folder='views')

        self.auth = core
        self.db = db

        #Start a Flask server in a thread
        self.server = threading.Thread(target=self.startServer)
        self.server.daemon = True
        self.server.start()

        #Start weview GUI
        self.webview = self.startWebview()


    def startServer(self):
        #self.config.from_object(config_by_name[config_name])
        self.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0# disable caching
        self.register_blueprint(flaskRoutes)
        self.run()

    def startWebview(self):
        webview.create_window("Trading App", "http://127.0.0.1:5000/")
        webview.start()
        return webview

    def update(self):
        pass
