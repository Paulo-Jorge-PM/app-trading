#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from abc import ABCMeta, abstractmethod
from core import authentication

#Abstract class: I used the abc library to turn python classes no abstract by default) into real abstract classes
class User(metaclass = ABCMeta):

    @abstractmethod
    def __init__(self, idUser, username, email, password, balance, userRole, dateRegistration):
        self.idUser = idUser
        self.username = username
        self.email = email
        self.password = password
        self.balance = balance
        self.userRole = userRole
        self.dateRegistration = dateRegistration
        #self.secureKey = None

    #@classmethod
    @abstractmethod
    def profile(self):
        pass

    @abstractmethod
    def editProfile(self):
        pass

    @abstractmethod
    def checkAuth(self):
        pass