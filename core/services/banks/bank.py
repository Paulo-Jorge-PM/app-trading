#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from abc import ABCMeta, abstractmethod
from core import authentication

class Bank(metaclass = ABCMeta):

	@abstractmethod
	def __init__(self):
		pass

	@abstractmethod
	def withdrawl():
		pass

	@abstractmethod
	def deposit():
		pass