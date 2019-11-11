#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod
from core import authentication
#from core import profile

class User(metaclass = ABCMeta):

    @abstractmethod
    def __init__(self):
        self.idUser = None
        self.name = None
        self.password = None
        self.email = None
        self.userRole = None

        self.secureToken = None


    #@classmethod
    @abstractmethod
    def checkAuth(self):
        pass

    @abstractmethod
    def editProfile(self):
        pass