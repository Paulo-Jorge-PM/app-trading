#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from abc import ABCMeta, abstractmethod
from core import authentication

class Broker(metaclass = ABCMeta):

	@abstractmethod
	def __init__(self):
		pass

	@abstractmethod
	def get_markets():
		pass

	@abstractmethod
	def get_transactions():
		pass

	@abstractmethod
	def get_prices():
		pass

	@abstractmethod
	def order():
		pass