#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import json
from flask import request
from oandapyV20 import API
import oandapyV20.endpoints.accounts as accounts
import oandapyV20.endpoints.trades as trades
import oandapyV20.endpoints.pricing as princing
import oandapyV20.endpoints.orders as orders

ACCOUNT_ID = "101-004-12680411-001"
ACESS_TOKEN = "a11f40a13ca614c4734457638ec24397-71367b8afff53618a06c22ecf2d1b23f"

def get_markets():
	client = API(access_token=ACESS_TOKEN)
	r = accounts.AccountInstruments(accountID=ACCOUNT_ID)
	rv = client.request(r)
	data = json.dumps(rv, sort_keys=True, indent=2)
	return data

#Portfolio
def get_transactions():
	client = API(access_token=ACESS_TOKEN)
	r = trades.TradesList(ACCOUNT_ID)
	rv = client.request(r)
	data = json.dumps(rv, sort_keys=True, indent=2)
	return data

#Atualizar/exibir preços com base na query no url
def get_prices():
	client = API(access_token=ACESS_TOKEN)
	#BID= SELL | ASKS = BUY
	instruments = request.args.get('instruments')
	#formato do ex: params = {"instruments" : "GBP_USD,XAG_CAD"}
	params = {"instruments" : instruments}
	r = princing.PricingInfo(accountID=ACCOUNT_ID, params=params)
	rv = client.request(r)
	data = json.dumps(rv, sort_keys=True, indent=2)
	return data

def order(instrument, units, takeProfit=0, stopLoss=0):
	#If positive units = buy ; if negative units = sell
	status_code = ""
	jsonResponse = ""
	client = API(access_token=ACESS_TOKEN)
	data = orderJson(instrument, units, takeProfit, stopLoss)
	print(data)
	r = orders.OrderCreate(accountID=ACCOUNT_ID, data=data)
	try:
		response = client.request(r)
	#except V20Error as e:
	#	print("V20Error: {}".format(e))
	except:
		print("Error - it failed")
	else:
		status_code = r.status_code
		jsonResponse = json.dumps(response, indent=2)
	return [status_code, jsonResponse]


def orderJson(instrument, units, takeProfit, stopLoss):
	order  = """{'order': {
	   'timeInForce': 'FOK',
	   'instrument': '""" + instrument + """',
	   'positionFill': 'DEFAULT',
	   'units': '""" + units + """',
	   'type': 'MARKET',
	   'takeProfitOnFill': {
	       'timeInForce': 'GTC',
	       'price': '""" + takeProfit + """'}
	   }
	   'stopLossOnFill': {
	       'timeInForce': 'GTC',
	       'price': '""" + stopLoss + """'}
		}
	}"""
	return order