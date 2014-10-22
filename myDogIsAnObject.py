#!/usr/bin/env python 
""" Object Oriented Code Review"""

class Dog:
	#What are the attributes of a person? 
	name = "Pumba"
	age = 0
	
	#add methods
	def setName(self, x):
		self.name = x
		
	def setAge(self, x):
		self.age = x
		
	def talk(self):
		print "My dog's name is", self.name, "and he is", self.age "years old."
		
	
myObject = Dog()
myObject.setName("Peter")
myObject.setAge(74)
myObject.talk()
