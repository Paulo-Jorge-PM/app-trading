#!/usr/bin/python
# -*- coding: UTF-8 -*-

from models import db
from core.services.banks import demo

class Money:

    def __init__(self, userId, currency="euros", bankType="demo"):
        self.balance = None
        self.userId = None
        self.currency = "euros"
        self.bankType = "demo"#to do: paypal, Visa, atm, etc. demo just to test for now
        self.db = db.Db()

    def getBalance(self):
        balance = db.Db().balance(self.userId)

        #Adapter: convert currency if user using other
        #since by default de DB always saves in euros, eurso are default
        if self.currency == "euros":
            return balance
        else:
            pass#to do currency converter calculations

        def updateBalance(self, newBalance):
            balance = self.db.balance(self.userId, newBalance)


    def widthdrawl(self, value):
        if bankType=="demo":
            bank = demo.Demo()
            transaction = bank.widthdrawl(value)
            if transaction == True:
                #save DB:
                self.db.widthdrawlBank(value)

                newBalance = getBalance() - value
                updateBalance(self.userId, newBalance)
                return True
            else:
                return False
                #message="Error! Something went wrong, your transaction could not be made."
                #return render_template("message.html", message=message)

    def deposit(self):
        pass