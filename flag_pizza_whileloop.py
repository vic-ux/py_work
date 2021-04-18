pizza_toppings = "\nEnter your choice of toppings:"
pizza_toppings += "\nEnter 'quit' when you are done requesting:"

topping = True
while topping :
	message = input(pizza_toppings)
	
	if message == 'quit':
		topping = False
	else:
		print ("\nI will add "+ message + " topping to your pizza.")
