#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import json
from flask import request
from oandapyV20 import API
import oandapyV20.endpoints.accounts as accounts
import oandapyV20.endpoints.trades as trades
import oandapyV20.endpoints.pricing as princing
import oandapyV20.endpoints.orders as orders
from oandapyV20.exceptions import V20Error
from oandapyV20.contrib.requests import (
    MarketOrderRequest,
    TakeProfitDetails,
    StopLossDetails
)
from core.services.brokers import broker

class Oanda(broker.Broker):
	def __init__(self):
		super().__init__()

		self.ACCOUNT_ID = "101-012-20885804-001"
		self.ACESS_TOKEN = "d7d011d085db85e7a249f62da2ce20bd-4a6118d7f6324a7989301d54b3517a2a"

	def get_markets(self):
		client = API(access_token=self.ACESS_TOKEN, environment="practice")#or pratice
		r = accounts.AccountInstruments(accountID=self.ACCOUNT_ID)
		rv = client.request(r)
		#data = json.dumps(rv, sort_keys=True, indent=2)
		return rv

	#Portfolio
	def get_transactions(self):
		client = API(access_token=self.ACESS_TOKEN, environment="practice")
		r = trades.TradesList(self.ACCOUNT_ID)
		rv = client.request(r)
		data = json.dumps(rv, sort_keys=True, indent=2)
		return data

	#Update/exibir prices com base na query get no url
	def get_prices(self, instruments):
		client = API(access_token=self.ACESS_TOKEN, environment="practice")
		#BID= SELL | ASKS = BUY
		#formato: params = {"instruments" : "GBP_USD,XAG_CAD,assetName,etc"}
		params = {"instruments" : instruments}
		r = princing.PricingInfo(accountID=self.ACCOUNT_ID, params=params)
		rv = client.request(r)
		#data = json.dumps(rv, sort_keys=True, indent=2)
		return rv

	def order(self, instrument, units, takeProfit=0, stopLoss=0):
		#If positive units = buy ; if negative units = sell
		status_code = ""
		jsonResponse = ""
		client = API(access_token=self.ACESS_TOKEN)

		# Order data JSON generate
		mktOrder = MarketOrderRequest(
			instrument=instrument,
			units=units,
			takeProfitOnFill=TakeProfitDetails(price=takeProfit).data,
			stopLossOnFill=StopLossDetails(price=stopLoss).data
		)

		data = mktOrder.data
		#data = json.loads(orderJson(instrument, units, takeProfit, stopLoss))
		print("Market Order specs: \n{}".format(json.dumps(data, indent=4)))

		r = orders.OrderCreate(accountID=self.ACCOUNT_ID, data=data)
		try:
			response = client.request(r)
		except V20Error as e:
			print(r.status_code, e)
			#print("V20Error: {}".format(e))
		else:
			status_code = r.status_code
			jsonResponse = json.dumps (response, indent=2)
			print("Response: {}\n{}".format(r.status_code, json.dumps(response, indent=2)))
		return [status_code, jsonResponse]


	#def orderJson(self, instrument, units, takeProfit, stopLoss):
	#	order  = """{'order': {
	#		'type': 'MARKET',
	#		'timeInForce': 'FOK',
	#		'instrument': '""" + instrument + """',
	#		'units': '""" + str(units) + """',
	#		'positionFill': 'DEFAULT',
	#		'stopLossOnFill': {
	#			'timeInForce': 'GTC',
	#			'price': '""" + str(stopLoss) + """'},
	#		'takeProfitOnFill': {
	#			'price': '""" + str(takeProfit) + """'}
	#		}
	#		}"""
	#	return order

