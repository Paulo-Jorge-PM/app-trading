#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Core import Movement
from Core import Investor

class Money(object):
    def getBalance(self):
        pass

    def makeMovement(self):
        pass

    def __init__(self):
        self.___balance = None
        """@AttributeType int"""
        self.___currency = None
        """@AttributeType string"""
        self.___user = None
        """@AttributeType <"""
        self._unnamed_Movement_ = []
        # @AssociationType Core.Movement[]
        # @AssociationMultiplicity 0..*
        self._unnamed_Investor_ = None
        # @AssociationType Core.Investor
        # @AssociationMultiplicity 1

