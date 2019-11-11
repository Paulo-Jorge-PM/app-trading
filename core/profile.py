#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Core import User

class Profile(object):
    def edit(self):
        pass

    def view(self):
        pass

    def setLanguage(self):
        pass

    def __init__(self):
        self.___user = None
        """@AttributeType <"""
        self.___name = None
        """@AttributeType string"""
        self.___email = None
        """@AttributeType string"""
        self.___password = None
        """@AttributeType string"""
        self.___defaultLang = None
        """@AttributeType string"""
        self._unnamed_User_ = None
        # @AssociationType Core.User

