#10.25.14Generators
import random

def get_data():
	#return 3 ints between 0 and 9
	return random.sample(range(10),3)

def consume():
	#display a running average 
	running_sum = 0
	data_items_seen = 0

	while True:
		data = yield
		data_items_seen += len(data)
		running_sum += sum(data)
		print ('The running average is {}'.format(running_sum / float(data_items_seen)))

def produce(consumer):
	#produce set and forwards them to predetermined function
	while True:
		data = get_data()
		print ('Produced {}'.format(data))
		consumer.send(data)
		yield

if __name__ == '__main__':
	consumer = consume()
	consumer.send(None)
	producer = producer(consumer)

	for _ in range(10)
		print ('Producing...')
		next(producer)
