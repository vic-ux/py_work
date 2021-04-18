topping = '\nEnter the kind of pizza toppings preffered'
topping += "\nEnter 'quit' to end request:"
request = ''
while request != 'quit':
	request = input(topping)
	if request != 'quit':
		print ('You will add ' + request + ' toppings to your pizza.')

	
	
