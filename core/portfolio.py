#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Core import Investor
from Core import Asset

class Portfolio(object):
    def viewHistory(self):
        pass

    def viewActives(self):
        pass

    def closeActive(self):
        pass

    def filter(self):
        pass

    def statistics(self):
        pass

    def recordinDB(self):
        pass

    def __init__(self):
        self.___transactions = None
        """@AttributeType list"""
        self.___user = None
        """@AttributeType <"""
        self._unnamed_Investor_ = None
        # @AssociationType Core.Investor
        # @AssociationMultiplicity 1
        self._unnamed_Asset_ = []
        # @AssociationType Core.Asset[]
        # @AssociationMultiplicity 0..*
        # @AssociationKind Composition

