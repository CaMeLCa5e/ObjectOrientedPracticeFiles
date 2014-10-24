
@decorator
def funtions(arg):
	return 'Return'

# this is the same as the first statement- 
def funtion(arg):
	return 'Return'
funtion = decorator(function) #passes funtion to decorator and reassigns it to the function. 

# a decorator is a function that takes a function and returns one.  would you call this a nested function? 

def repeater(old_function):
	def new_function(*args, **kwds):
		old_function(*args, **kwds)# old function
		old_function(*args, **kwds) #do it again for illistration 
	return new_function  


@repeater
def Multiply(num1, num2):
	print num1*num2


def Double_Out (old_function):
	def new_function(*args, **kwds):
		return 2*old_function(*args, **kwds)
	return new_function

def Double_in(old_function):
	def new_function(arg):
		return old_function(arg*2)
	return new_function

def Check(old_function):
	def new_finction(arg):
		if arg<0: raise ValueError, "Negative Argument"
		old_function(arg)
	return new_function

def multiply(multiplier):
	def Multiply_Generator(old_function):
		def new_function(*args, **kwds):
			return new_function	
return Multiply_Generator

@Multiply(3) 
def Num(num):
	return num














