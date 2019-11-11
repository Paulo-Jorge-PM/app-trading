#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Core import Market
from Core import Asset

class BrokerApi(object):
    def connect(self):
        pass

    def getHistory(self):
        pass

    def buyAsset(self):
        pass

    def sellAsset(self):
        pass

    def checkAsset(self):
        pass

    def getAssets(self):
        pass

    def __init__(self):
        self.___acessToken = None
        """@AttributeType string"""
        self.___acessAuth = None
        """@AttributeType string"""
        self.___user = None
        """@AttributeType <"""
        self.___brokerUri = None
        """@AttributeType string"""
        self._unnamed_Market_ = None
        # @AssociationType Core.Market
        # @AssociationMultiplicity 1
        self._unnamed_Asset_ = None
        # @AssociationType Core.Asset
        # @AssociationMultiplicity 1

