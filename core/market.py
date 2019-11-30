#!/usr/bin/python
# -*- coding: UTF-8 -*-

import datetime
import json
from flask import current_app
from core import investor
from core.services.brokers import oanda
from models import db

#Adapter design Pattern
#Markets have some methods that works as an Adapter for the Brokers API ()
#Objective: we can change the broker api provider anytime, 
#But the core.markets interface will always work without breaking the app,
#Because it always returns the same type of data and adapts it from the api provider to the app expected

class Market:

    def __init__(self, idUser):
        #self.assets = None
        self.user = idUser
        self.db = db.Db()
        #To do: Get Broker API in use from a configuration file and allow the user to change preferences
        #self.brokerApi = current_app.config.BROKER_API
        self.brokerApi = 'oanda'

        self.broker = None
        if self.brokerApi == 'oanda':
            self.broker = oanda.Oanda()

    def order(self, orderType, instrument, units, takeProfit, stopLoss, displayName, marketType):
        if self.brokerApi == "oanda":
            #Validate data for the Oanda Json formata
            units = float(units.replace(",", "."))
            takeProfit = float(takeProfit.replace(",", "."))
            stopLoss = float(stopLoss.replace(",", "."))

            if orderType == "sell":
                #Oanda API for sell uses negative number, for buy positive ones
                #So we need to adapt the data
                if units > 0:
                    units = units * -1
            else:
                if units < 0:
                    #If buy, and if units negative, make it positive
                    units = units * -1

            order = self.broker.order(instrument, units, takeProfit, stopLoss)
            #Check if Oanda answered with positve order deal
            #Oanda give 2 variables: status code (201 = success) and a Json summary of the transaction
            #We receive it as a list here from the API
            #And save in DB and return
            if order[0] == 201:
                startValue = 0
                saveDb = self.saveOrder(instrument, units, orderType, takeProfit, stopLoss, startValue, displayName, marketType)
                if saveDb == True:
                    return True
                else:
                    #Estes prints em produção deveria mser convertidos em logs
                    print("Error - API worked but DB not for user xx!")
                    return False
            else:
                return False


    def saveOrder(self, instrument, units, orderType, takeProfit, stopLoss, startValue, displayName, marketType):
        dateTransac = datetime.datetime.now()
        try:
            self.db.insertAsset(userId=self.user, assetId=instrument, units=units, displayName=displayName, marketType=marketType, orderType=orderType, takeProfit=takeProfit, stopLoss=stopLoss, startValue=startValue, dateTransac=dateTransac)
            return True
        except Exception as error:
            print(error)
            return False


    def closeAsset(self, idAsset):
        if self.brokerApi == "oanda":
            #To do: close also in the API
            pass
        #Save DB
        try:
            self.db.closeAsset(idAsset)
            return "True"
        except Exception as error:
            #To do: pass the print to a log file instead
            print(error)
            return "False"
        

    def getAssets(self):
        #Adapter for different broker API's and converter into Json for the views
        if self.brokerApi == "oanda":
            try:
                data = self.broker.get_markets()
                data2json = json.dumps(data, sort_keys=True, indent=2)
                return data2json
            except Exception as error:
                print(error)
                return False

    def getPrices(self, instruments):
        #Adapter for different broker API's and converter into Json for the views
        if self.brokerApi == "oanda":
            try:
                data = self.broker.get_prices(instruments)
                data2json = json.dumps(data, sort_keys=True, indent=2)
                return data2json
            except Exception as error:
                print(error)
                return False
