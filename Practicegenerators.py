#Practice with generators
def simple_generator_function():
	yield 1
	yield 2
	yield 3

for value in simple_generator_function():
	print (value)

our_generator = simple_generator_function()
print next(our_generator)

#the next two blocks push the generator to exhaustion. 
# def get_primes(number):
# 	while True:
# 		if is_prime(number):
# 			yield number
# 		number += 1

# our_generator = simple_generator_function()
# for value in our_generator:
# 	print value
# print (next(our_generator))

def solve_number_10():
	total = 2
	for next_prime in get_primes(3):
		if next_prime < 2000000:
			total += next_prime
		else:
			print (total)
			return
def get_primes(number):
	while True:
		if is_prime(number):
			yield number
		number += 1


def print_successive_primes(iterations, base = 10):

	prime_generator = get_primes(base)
	for power in range(iterations):
def get_primes(number):
	while True:
		if is_prime(number):
			number = yield number
		number += 1


def get_primes(number):
	while True:
		if is_prime(number):
			number = yield number
		number += 1

def print_successive_primes(iterations, base = 10):
	prime_generator = get_primes(base)
	prime_generator.send(None)
	for power in range(iterations):
		print(prime_generator.send(base**power))

		






