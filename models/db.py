#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
pydal : ORM / Database Abstraction Layer
Here I define the schemas and inttialize the DB
In the controllers we interact with it trough self.db
"""

from pydal import DAL, Field

import os
#path absolute and independet to the OS, so it works in any
current_dir = os.path.dirname(os.path.abspath(__file__))

class Db:

    def __init__(self):
        self.uri = 'sqlite://database.sqlite'
        self.folder = os.path.join(current_dir, "storage")

        self.db = None

    def connect(self):
        if not self.db:
            self.db = DAL(self.uri, folder=self.folder, pool_size=5, lazy_tables=True)
            #, migrate_enabled=False, migrate=False, lazy_tables=True
            self.tables()
        else:
            print("Error: db already open")

    def close(self):
        #if self.db:
        #    self.db.close()
        #    self.db = None
        self.db.close()
        self.db = None

    def tables(self):
        self.tableUsers()
        self.tableAssets()
        self.tableBank()

    def tableUsers(self):
        try:
            #Note: id is created automattically if omited
            self.db.define_table('users', 
                Field('username', type='string'), 
                Field('email', type='string'),
                Field('password', type='string'),
                Field('balance', type='integer', default=0),
                Field('userRole', type='string', defaul='user'),#user, admin
                Field('secureKey', type='string', default='0', writable=False, readable=False),#not used for now - it should be in a server-side not acessible
                Field('dateRegistration', type='datetime', writable=False, readable=False)
                )
        except:
            print('models db.DB() tableUsers Error')

    def tableAssets(self):
        try:
            self.db.define_table('assets', 
                Field('userId', type='integer'), 
                Field('assetId', type='string'),#asset name id
                Field('units', type='integer'),#units; negative == sell; positive == buy
                Field('assetName', type='string'),#asset display name
                Field('marketType', type='string'),#CURRENCY, METAL, CFD etc
                Field('action', type='string'),#buy/ask or sell/bid
                Field('takeProfit', type='integer', default=0),#takeProfit limit? 0 = no
                Field('stopLoss', type='integer', default=0),#takeLoss limit? 0 = no
                Field('closed', type='boolean', default=False),#open or close
                Field('startValue', type='integer'),#price
                Field('closeValue', type='integer'), 
                Field('dateTransac', type='datetime', writable=False, readable=False)
                )
        except:
            print('models db.DB() tableAssets Error')

    def tableBank(self):
        try:
            self.db.define_table('bank', 
                Field('userId', type='integer'), 
                Field('value', type='integer'),#euros
                Field('action', type='string'),#deposit or widhtrawl
                Field('balanceBefore', type='integer'),
                Field('transitionType', type='string', default='nib'),#paypal,nib,credit card etc
                Field('bankId', type='integer', writable=False, readable=False),#iban f.e. etc. to do: add more
                Field('dateTransac', type='datetime', writable=False, readable=False)
                )
        except:
            print('models db.DB() tableBaknk Error')


    def insertUser(self, username, email, password, dateRegistration):
        self.connect()
        import secrets#generate url safe token
        secureKey = secrets.token_urlsafe()
        self.db.users.insert(username=username, email=email, password=password, balance=0, userRole="user", secureKey=secureKey, dateRegistration=dateRegistration)
        self.db.commit()
        self.db.close()

    def insertAsset(self, userId, assetId, units, displayName, marketType, orderType, takeProfit, stopLoss, startValue, dateTransac):
        self.connect()
        self.db.assets.insert(userId=userId, assetId=assetId, units=units, assetName=displayName, marketType=marketType, action=orderType, takeProfit=takeProfit, stopLoss=stopLoss, startValue=startValue, dateTransac=dateTransac, closed=False, closeValue=0)
        self.db.commit()
        self.db.close()


    def loginUser(self, username, password):
        self.connect()
        self.db._adapter.reconnect()#gives thread error without
        user = self.db( (self.db.users.username == username) & (self.db.users.password == password) ).select().first()
        self.db.close()
        #if no user, user = None
        return user

    def portfolio(self, userId):
        self.connect()
        portfolio = self.db(self.db.assets.userId == userId).select()
        self.db.close()
        return portfolio

    def closeAsset(self, idAsset):
        self.connect()
        row = self.db(self.db.assets.id == idAsset).select().first()
        row.update_record(closed=True)
        self.db.close()

    def balance(self, userId):
        self.connect()
        user = self.db(self.db.users.id == userId).select().first()
        balance = user["balance"]
        self.db.close()
        return balance

    def updateBalance(userId, newBalance):
        self.connect()
        user = self.db(self.db.users.id == userId).select().first()
        user.update_record(balance=newBalance)
        self.db.close()