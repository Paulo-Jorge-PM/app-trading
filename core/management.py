#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Core import Admin

class Management(object):
    def getUsers(self):
        pass

    def blockUser(self):
        pass

    def getTransactions(self):
        pass

    def getMoney(self):
        pass

    def analysis(self):
        pass

    def __init__(self):
        self.___users = None
        """@AttributeType list"""
        self.___transactions = None
        """@AttributeType list"""
        self.___moneyMovs = None
        """@AttributeType list"""
        self._unnamed_Admin_ = None
        # @AssociationType Core.Admin
        # @AssociationMultiplicity 1

