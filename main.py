#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from core import authentication
from ui.webview import gui
from models import db

#from models import orm

class Main:

    def __init__(self):

        #Layered: the view see the controllers, the controllers see the models

        #Start Core layer (inside it we start and call the DB ORM)
        self.auth = authentication.Authentication()
    

        #Start GUI layer and gie the Core to it
        self.gui = gui.Gui(core=self.auth)

        #Start DB ORM layer
        #self.db = db.Db()
        
    
    def upgrade(self):
        #TODO: Check if there is new version of the app and upgrade
        pass

if __name__ == '__main__':
    main = Main()