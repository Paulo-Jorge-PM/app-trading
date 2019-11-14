#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from core import authentication
from ui.webview import gui

#from models import orm

class Main:

    def __init__(self):
        #Start Core layer
        self.auth = authentication.Authentication()
        
        #Start DB ORM layer
        self.db = "teste"

        #Start GUI layer
        self.gui = gui.Gui(core=self.auth, db=self.db)
        
    
    def upgrade(self):
        #TODO: Check if there is new version of the app and upgrade
        pass

if __name__ == '__main__':
    main = Main()