#!/usr/bin/python3
# -*- coding: UTF-8 -*-

#from core import money
#from core import market
#from core import portfolio
from core import user
from models import db

class Investor(user.User):

    #def __init__(self, username, email, password, userRole):
    def __init__(self, idUser, username, email, password, balance, userRole, dateRegistration):
        super().__init__(idUser, username, email, password, balance, userRole, dateRegistration)
        self.userRole = "user"
        self.balance = 500

    def portfolio(self):
        portfolio = db.Db().portfolio(self.idUser)
        return portfolio

    def buy(self):
        pass

    def sell(self):
        pass

    def checkAuth(self):
        pass
    
    def profile(self):
        pass

    def editProfile(self):
        pass

    def getBalance(self):
        pass

    def viewMarkets(self):
        pass





