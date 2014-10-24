def do_stuff_with_number(n):
	print n

the_list = (1,2,3,4,5)

for i in range(20):
	try:
		do_stuff_with_number(the_list[i])
	except IndexError: #this will show when there is something out of range
		do_stuff_with_number(0)