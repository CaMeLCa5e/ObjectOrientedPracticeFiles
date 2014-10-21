#!/usr/bin/env python 
"""OO walkthrough
"""

class pet:
	number_of_legs = 0
	
	def sleep(self):
		print 'zzz'
		
	def count_legs(self):
		print 'Pumba has %s legs' %self.number
		
class dog(pet):
	def bark(self):
		print "Woof"
		
		
		
pumba = dog()
pumba.bark()
pumba.sleep()
pumba.number_of_legs = 4
# pumba.count_legs()
print "Pumba has %s legs." % pumba.number_of_legs