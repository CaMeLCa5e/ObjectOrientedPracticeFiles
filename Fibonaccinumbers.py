"""Playing with Fibonacci numbers
"""

def F(n):
	#Time 0(2**n), Space 0(n)
	if n < 2: return n
	else: F(n-1) + F(n-2)


#########
# another way:

# Time 0(n), Space(n)
def F(n):
	a, b = 0, 1
	for i in range(0, n):
		a, b = b, a + b
	return a

###
#yet another way 0(1) for Time and Space
import math
def F(n):
	return ((1+math.sqrt(5))**n-(1-math.sqrt(5))**n)/(2**n*math.sqrt(5))
