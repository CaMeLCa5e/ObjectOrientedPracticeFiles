"""Static methods (car)"""

class Vehicle(object):
	@classmethod
		def is_motorcycle(cls):
			return cls.wheels == 2

	base_sale_price = 0

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

	def __init__(self, wheels, miles, make, model, year, sold_on):
		self.wheels = wheels
		self.miles = miles	
		self.make = make
		self.model = model
		self.year = year
		self.sold_on = sold_on

class Truck(Vehicle):

	def __init__(self, wheels, miles, make, model, year, sold_on):
		self.wheels = wheels
		self.miles = miles
		self.make = make
		self.model = model
		self.year = year
		self.sold_on = sold_on
		self.base_sale_price = 10000

	def sale_price(self):
		if self.sold_on is not None:
			return 0.0 
		return 5000.0 * self.wheels

	def purchase_price(self):
		if self.sold_on is None:
			return 0.0 
		return 8000 - (.10 *self.miles)

	@staticmethod
	def make_car_sound():
		print 'VROOOOOOOMMMMM'


