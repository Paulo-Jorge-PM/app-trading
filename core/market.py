#!/usr/bin/python
# -*- coding: UTF-8 -*-
from core import investor
#from services import brokerApi
from services.brokers import oanda
from flask import current_app

#Adapter design Pattern
#Markets have some methods that works as an Adapter for the Brokers API ()
#Objective: we can change the broker api provider anytime, 
#But the core.markets interface will always work without breaking the app,
#Because it always returns the same type of data and adapts it from the api provider to the app expected

class Market:

    def __init__(self):
        self.assets = None

        self.user = None

        #To do: Get Broker API in use from a configuration file and allow the user to change preferences
        #self.brokerApi = current_app.config.BROKER_API
        self.brokerApi = 'oanda'

    def order(self, orderType, instrument, units, takeProfit=0, stopLoss=0):

        if self.brokerApi == "oanda":
            if orderType == "sell":
                #Oanda API for sell uses negative number, for buy positive ones
                #So we need to adapt the data
                if units > 0:
                    units = units * -1
            else:
                if units < 0:
                    #If buy, and if units negative, make it positive
                    units = units * -1

            order = oanda.order(instrument, units, takeProfit, stopLoss)
            #Check if Oanda answered with positve order deal
            #Oanda give 2 variables: status code (201 = success) and a Json summary of the transaction
            #We receive it as a list here from the API
            print(order[0])

            if order[0] == 201:
                return True
            else:
                return False

    def getAssets(self):
        pass

    def investment(self):
        pass

    def getStatistics(self):
        pass

    def filter(self):
        pass




