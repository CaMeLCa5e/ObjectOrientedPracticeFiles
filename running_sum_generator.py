#running sum generator

def consume():
	#display a running average 
	running_sum = 0
	data_items_seen = 0

	while True:
		data = yield
		data_items_seen += len(data)
		running_sum += sum(data)
		print ('The running average is {}'.format(running_sum / float(data_items_seen)))