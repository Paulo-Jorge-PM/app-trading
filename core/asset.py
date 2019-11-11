#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Core import Market
from Core import Portfolio
from Services import BrokerApi

class Asset(object):
    def buy(self):
        pass

    def sell(self):
        pass

    def close(self):
        pass

    def recordInDb(self):
        pass

    def updateCheck(self):
        pass

    def __init__(self):
        self.___assetData = None
        """@AttributeType list"""
        self.___cFDContractId = None
        """@AttributeType int"""
        self.___user = None
        """@AttributeType <"""
        self.___takeProfit = None
        """@AttributeType int"""
        self.___stopLoss = None
        """@AttributeType int"""
        self.___closed = None
        """@AttributeType boolean"""
        self.___quantity = None
        """@AttributeType string"""
        self.___transactionType = None
        """@AttributeType string"""
        self.___aquisitionPrice = None
        """@AttributeType int"""
        self.___closePrice = None
        """@AttributeType int"""
        self.___leverage = None
        """@AttributeType int"""
        self._unnamed_Market_ = None
        # @AssociationType Core.Market
        # @AssociationMultiplicity 1
        self._unnamed_Portfolio_ = None
        # @AssociationType Core.Portfolio
        # @AssociationMultiplicity 1
        self._unnamed_BrokerApi_ = None
        # @AssociationType Services.BrokerApi
        # @AssociationMultiplicity 1

