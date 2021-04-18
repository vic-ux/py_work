pizza_toppings = "\nEnter your choice of toppings:"
pizza_toppings += "\nEnter 'quit' when you are done requesting:"

message = " "
while message != 'quit':
	message = input(pizza_toppings)
	
	
	
	if message != 'quit':
		print ("\nI will add "+ message + " topping to your pizza.")
