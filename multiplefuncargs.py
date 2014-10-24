#multiple function arguments. 
def foo(first, second, third, *therest):
	print "First: %s" % first
	print "Second: %s" % second
	print "Third: %s" % third
	print "and all the rest... %s" % list(therest)

#now try sending words through key word

def bar(first, second, third, **options):
	if options.get('action') == "sum":
		print "The sum is: %d" % (first + second + third)

	if options.get('number') == 'first':
		return first

result = bar(1,2,3, action = 'sum', number = 'first')
print "Result: %d" % result
