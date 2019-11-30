#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from core import authentication

#from models import db

#from models import orm

class Main:

    def __init__(self):

        self.configs = self.readConfigs()

        #Start Core layer 
        self.auth = authentication.Authentication(self.configs)
    
        #Start GUI layer and give the core entry to it
        self.gui = self.setGui()

        #Start DB ORM layer
        #self.db = db.Db()
        
    def readConfigs(self):
        #to do: read constants from the config file in core/tools instead of declaring here
        broker = "oanda"
        gui = "webview"
        banks = ["demo", "paypal"]
        return(gui, broker, banks)

    def setGui(self):
        if self.configs[0] == "webview":
            from ui.webview import gui
        #here one can define what GUI package to use
        else:
            #Note: terminal not implemented, only an empty class
            from ui.webview import gui
        self.gui = gui.Gui(core=self.auth)

    def upgrade(self):
        #TODO: Check if there is new version of the app and upgrade
        pass

if __name__ == '__main__':
    main = Main()