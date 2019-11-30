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

ACCOUNT_ID = "101-004-12680411-001"
ACESS_TOKEN = "a11f40a13ca614c4734457638ec24397-71367b8afff53618a06c22ecf2d1b23f"

def get_markets():
	client = API(access_token=ACESS_TOKEN)
	r = accounts.AccountInstruments(accountID=ACCOUNT_ID)
	rv = client.request(r)
	#data = json.dumps(rv, sort_keys=True, indent=2)
	return rv

#Portfolio
def get_transactions():
	client = API(access_token=ACESS_TOKEN)
	r = trades.TradesList(ACCOUNT_ID)
	rv = client.request(r)
	data = json.dumps(rv, sort_keys=True, indent=2)
	return data

#Update/exibir prices com base na query get no url
def get_prices(instruments):
	client = API(access_token=ACESS_TOKEN)
	#BID= SELL | ASKS = BUY
	#formato: params = {"instruments" : "GBP_USD,XAG_CAD,assetName,etc"}
	params = {"instruments" : instruments}
	r = princing.PricingInfo(accountID=ACCOUNT_ID, params=params)
	rv = client.request(r)
	#data = json.dumps(rv, sort_keys=True, indent=2)
	return rv

def order(instrument, units, takeProfit=0, stopLoss=0):
	#If positive units = buy ; if negative units = sell
	status_code = ""
	jsonResponse = ""
	client = API(access_token=ACESS_TOKEN)

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

	r = orders.OrderCreate(accountID=ACCOUNT_ID, data=data)
	try:
		response = client.request(r)
	except V20Error as e:
		print(r.status_code, e)
		#print("V20Error: {}".format(e))
	else:
		status_code = r.status_code
		jsonResponse = json.dumps(response, indent=2)
		print("Response: {}\n{}".format(r.status_code, json.dumps(response, indent=2)))
	return [status_code, jsonResponse]


#def orderJson(instrument, units, takeProfit, stopLoss):
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

