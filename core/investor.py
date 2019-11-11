#!/usr/bin/python
# -*- coding: UTF-8 -*-

#from core import money
#from core import market
#from core import portfolio
from core import user

class Investor(user.User):

    #def __init__(self, name, email, password, userRole):
    def __init__(self):
        super().__init__()
        self.balance = 100000000000

        print(self.balance)


    def checkAuth(self):
        pass

    
    def editProfile(self):
        pass

    def editProfile(self):
        pass

    def getBalance(self):
        pass

    def viewMarkets(self):
        pass





