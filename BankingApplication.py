"""Banking application for building a checking account.  Customers have
the following attributes: name and balance. 
"""
class Customer(object):

	def __init__ (self, name, name:
		self.name = name
		self.balance = 0.0

	def set_balance(set, balance=0.0)
		self.balance = balance

	def withdraw(self, amount):
		if amount > self.balance:
			raise RuntimeErrot("amount greater than available")

	def deposit(self, amount):
		self.balance += amount
		return self.balance

