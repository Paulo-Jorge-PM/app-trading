#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json
import oandapyV20
import oandapyV20.endpoints.accounts as accounts

ACCOUNT_ID = "101-012-20885804-001"
ACESS_TOKEN = "d7d011d085db85e7a249f62da2ce20bd-4a6118d7f6324a7989301d54b3517a2a"

client = oandapyV20.API(access_token=ACESS_TOKEN)

r = accounts.AccountInstruments(accountID=ACCOUNT_ID)
rv = client.request(r)
print(json.dumps(rv, indent=2))
