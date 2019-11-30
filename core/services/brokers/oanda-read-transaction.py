#!/usr/bin/python
# -*- coding: UTF-8 -*-

import configparser
from oandapyV20 import API
from oandapyV20.endpoints.transactions import TransactionsStream
from oandapyV20.exceptions import V20Error, StreamTerminated

ACCOUNT_ID = "101-004-12680411-001"
ACESS_TOKEN = "a11f40a13ca614c4734457638ec24397-71367b8afff53618a06c22ecf2d1b23f"

#Config
#config = configparser.ConfigParser()
#config.read('oanda.cfg')

#api = API(environment='practice', access_token=config['oanda']['access_token'])

api = API(access_token=ACESS_TOKEN, environment="practice")

#request = PricingStream(accountID=accountID, params={"instruments": ",".join(clargs.instruments)})

request = TransactionsStream(accountID=ACCOUNT_ID)

MAXTRANS = 10

print("read from stream until {} transactions received".format(MAXTRANS))
try:
    n = 0
    for R in api.request(request):
        print(R)
        n += 1
        if n > MAXTRANS:
            s.terminate("max transactions received")

except StreamTerminated as e:
    print("{}".format(e))
except V20Error as e:
    print("Error: {}".format(e))
    
#Start        
#data = oanda.get_history(instrument='EUR_USD', start='2016-12-08', end='2016-12-10', granularity='M1')
                         
#print(data)
