"""Static methods (car)"""
from abc import ABCMeta, abstractmethod
class Vehicle(object):

	__metaclass__ = ABCMeta

	
	base_sale_price = 0
	wheels = 0 

	def __init__(self, wheels, miles, make, model, year, sold_on):
		self.wheels = wheels
		self.miles = miles
		self.make = make
		self.model = model
		self.year = year
		self.sold_on = sold_on

	def sale_price(self):
		if self.sold_on is not None:
			return 0.0
		return 5000.0 * self.wheels

	def purchase_price(self):
		if self.sold_on is None:
			return 0.0 
		return self.base_sale_price - (.10 * self.miles)


	
class Car(Vehicle):

	# def __init__(self, wheels, miles, make, model, year, sold_on):
	# 	self.wheels = wheels
	# 	self.miles = miles	
	# 	self.make = make
	# 	self.model = model
	# 	self.year = year
	# 	self.sold_on = sold_on

	base_sale_price = 8000
	wheels = 4
	def vehicle_type(self):
		return 'car'

class Truck(Vehicle):

	# def __init__(self, wheels, miles, make, model, year, sold_on):
	# 	self.wheels = wheels
	# 	self.miles = miles
	# 	self.make = make
	# 	self.model = model
	# 	self.year = year
	# 	self.sold_on = sold_on
	# 	self.base_sale_price = 10000
	
	base_sale_price = 10000
	wheels = 4

	def sale_price(self):
		if self.sold_on is not None:
			return 0.0 
		return 5000.0 * self.wheels

	def purchase_price(self):
		if self.sold_on is None:
			return 0.0 
		return 8000 - (.10 *self.miles)
	
	def vehicle_type(self):
		return 'truck'

class Motorcycle(Vehicle):

	base_sale_price = 4000
	wheels = 2

	def vehicle_type(self):
		return 'Motorcycle'

@abstractmethod
def vehicle_type():
	pass

@classmethod
def is_motorcycle(cls):
	return cls.wheels == 2

@staticmethod
def make_car_sound():
	print 'VROOOOOOOMMMMM'


