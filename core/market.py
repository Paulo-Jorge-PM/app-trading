#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Core import Investor
from Services import BrokerApi
from Core import Asset

class Market(object):
    def getAssets(self):
        pass

    def investment(self):
        pass

    def getStatistics(self):
        pass

    def filter(self):
        pass

    def __init__(self):
        self.___assets = None
        """@AttributeType list"""
        self.___user = None
        """@AttributeType <"""
        self._unnamed_Investor_ = None
        # @AssociationType Core.Investor
        # @AssociationMultiplicity 1
        self._unnamed_BrokerApi_ = None
        # @AssociationType Services.BrokerApi
        # @AssociationMultiplicity 1
        self._unnamed_Asset_ = []
        # @AssociationType Core.Asset[]
        # @AssociationMultiplicity 0..*
        # @AssociationKind Composition

