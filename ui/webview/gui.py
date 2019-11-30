#!/usr/bin/python3
# -*- coding: UTF-8 -*-

#To do: finish translation package, not used yet
from ui.internationalization import internationalization

from flask import Flask
from ui.webview.controllers.routes import flaskRoutes
from core.tools.scripts import screen

import webview
import sys
import threading

class Gui(Flask):
    def __init__(self, import_name=__name__, core=None):
        super(Gui, self).__init__(import_name=__name__, static_folder='static', template_folder='views')

        #I opted to inherit and call the builder of Flask here intentionally: this is not usuall procedding
        #Usually it is just an import and call p.e. app = Fask() and done
        #I did this subclassing so I could manippulate the initallization context of Flask
        #So now auth (core entry) and it's context (db (models entry) etc) are global trough the Flask.current_app context builder
        #Other design decisions were opted here: f.e. using blueprints, a kind of Decorator that let me use routes out of Flask app context
        self.auth = core

        #Start a Flask server in a thread
        self.server = threading.Thread(target=self.startServer)
        self.server.daemon = True
        self.server.start()

        #Start weview GUI
        self.webview = self.startWebview()


    def startServer(self):
        #CONFIGURATIONS
        #self.config.from_object(config_by_name[config_name])
        self.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0# disable caching so it refresh the view in each start
        self.configApp()

        #DECORATOR PATTERN that extends the routes
        #Here I used the blueprints for the decorator design pattern so I could use routes outside the Flask app context as glue like controllers
        self.register_blueprint(flaskRoutes)

        #threaded=False for the connection pools, because of a bug with the DAL library,
        #But also because we work with a single user locally in the app, no need for multi-pooling
        self.run(debug=False, threaded=False)

    def startWebview(self):
        #I want the app to start maximized. I had to use other Gui like tkinter to get the screen size before innitialization
        resolution = screen.Screen().getResolution()
        webview.create_window("Trading App", "http://127.0.0.1:5000/", width=resolution[0], height=resolution[1])
        webview.start()
        return webview

    #Pre-configurations. want to use other router api or GUI framework? just change these and voilà
    def configApp(self):
        self.config.update(
            BROKER_API = "oanda",
            BANK_API = "paypal",
            GUI = "webview"
            )


    def update(self):
        pass

