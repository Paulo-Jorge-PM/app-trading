#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Core import Management
from Core import User

class Admin(User):
    def manage(self):
        pass

    def editProfile(self):
        pass

    def __init__(self):
        self.___action = None
        """@AttributeType string"""
        self._unnamed_Management_ = None
        # @AssociationType Core.Management
        # @AssociationMultiplicity 1

