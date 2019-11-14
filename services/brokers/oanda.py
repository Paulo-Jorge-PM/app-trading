#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json
import oandapyV20
import oandapyV20.endpoints.accounts as accounts

ACCOUNT_ID = "101-004-12680411-001"
ACESS_TOKEN = "a11f40a13ca614c4734457638ec24397-71367b8afff53618a06c22ecf2d1b23f"

def get_markets():
	client = oandapyV20.API(access_token=ACESS_TOKEN)
	r = accounts.AccountInstruments(accountID=ACCOUNT_ID)
	rv = client.request(r)
	data = json.dumps(rv, sort_keys=True, indent=2)

	#return rv
	return data