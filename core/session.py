#!/usr/bin/python
# -*- coding: UTF-8 -*-
class Session(object):
    def startSession(self):
        pass

    def checkSession(self):
        pass

    def destroySession(self):
        pass

    def __init__(self):
        self.___user = None
        """@AttributeType <"""
        self.___securityKey = None
        """@AttributeType string"""
        self.___state = None
        """@AttributeType string"""

