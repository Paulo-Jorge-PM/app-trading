#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import datetime
from models import db

from core import investor
#from core import admin
#from core import session

#dal = db.Db()

class Authentication:

    def __init__(self):
        self.db = db.Db()

        self.user = None
        self.loginStatus = False

        #self.checkSession()

    def login(self, username, password):
        user = self.db.loginUser(username,password)
        if user:
            if user["userRole"] == "user":
                self.user = investor.Investor(user["id"], user["username"], user["email"], user["password"], user["balance"], user["userRole"], user["dateRegistration"])
            elif user["userRole"] == "admin":
                self.user = admin.Admin(user["id"], user["username"], user["email"], user["password"], user["balance"], user["userRole"], user["dateRegistration"])

            self.loginStatus = True
            return True
        else:
            self.user = None
            self.loginStatus = False
            return False

    def register(self, name, email, password):
        dateReg = datetime.datetime.now()
        try:
            self.db.insertUser(username=name, email=email, password=password, dateRegistration=dateReg)
            return True
        except Exception as error:
            print(error)
            return False

    def logout(self):
        self.user = None
        self.loginStatus = False

    def lostPassword(self):
        pass

    def creatUser(self):
        #self.user = investor.Investor(name, email, password, userRole="investor")
        self.user = investor.Investor()

    def creatAdmin(self):
        #self.user = investor.Investor(name, email, password, userRole="investor")
        self.user = admin.Admin()

    def setSession(self):
        pass

    def destroySession(self):
        pass

    def checkSession(self):
        pass

