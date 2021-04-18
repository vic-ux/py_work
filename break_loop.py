pizza_toppings = "\nEnter your choice of toppings:"
pizza_toppings += "\nEnter 'quit' when you are done requesting:"

while True:
	message = input(pizza_toppings)
	
	if message == 'quit':
		break
	else:
		print ("\nI will add "+ message + " topping to your pizza.")





