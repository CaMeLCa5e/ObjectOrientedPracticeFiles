"""Practice in OO"""

class pet:
	number_of_legs = 0 

	def sleep(self):
		print "ZzZzZzZzZzZzZ"

	def count_legs(self):
		print "I have %s legs" %self.number_of_legs
class dog(pet):
	def bark(self):
		print "Woof"

charles = pet()
charles.number_of_legs = 4
charles.count_legs()

nemo = pet()
nemo.number_of_legs = 0
nemo.count_legs()

doug = dog()
doug.number_of_legs = 4
doug.count_legs()



