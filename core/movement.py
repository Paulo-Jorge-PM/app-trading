#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Core import Money
from Services import PaymentApi

class Movement(object):
    def deposit(self):
        pass

    def withdrawl(self):
        pass

    def recordInDb(self):
        pass

    def __init__(self):
        self.___value = None
        """@AttributeType int"""
        self.___moveDate = None
        """@AttributeType datetime"""
        self.___transferType = None
        """@AttributeType string"""
        self.___user = None
        """@AttributeType <"""
        self._unnamed_Money_ = None
        # @AssociationType Core.Money
        # @AssociationMultiplicity 1
        self._unnamed_PaymentApi_ = None
        # @AssociationType Services.PaymentApi
        # @AssociationMultiplicity 1

