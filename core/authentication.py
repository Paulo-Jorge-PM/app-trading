#!/usr/bin/python
# -*- coding: UTF-8 -*-

from core import investor
#from core import admin
#from core import session

class Authentication:

    def __init__(self):
        self.user = None
        self.loginStatus = bool

        self.checkSession()

        if self.loginStatus == True:
            pass
        else:
            pass




    def login(self, email, password):
        if email == "p" and password == "1":
            self.loginStatus == True
            self.user()
            return True
        else:
            self.loginStatus == False
            return False

    def register(self):
        return "Registar"

    def lostPassword(self):
        pass

    def logout(self):
        self.user == None

    def user(self):
        #self.user = investor.Investor(name, email, password, userRole="investor")
        self.user = investor.Investor()

    def setSession(self):
        pass

    def destroySession(self):
        pass

    def checkSession(self):
        pass

