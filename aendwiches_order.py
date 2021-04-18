sandwich_order = []
sandwich_order.append('tuna')
sandwich_order.append('beef')
sandwich_order.append('pastrami')
sandwich_order.append('chicken')
sandwich_order.append('pastrami')
sandwich_order.append('fish')
sandwich_order.append('cheese')
print(sandwich_order)
finished_sandwiches = []
while sandwich_order:
	sandwich_orders = sandwich_order.pop()
	print ("\nI made you a " + sandwich_orders + " sandwich.")
	finished_sandwiches.append(sandwich_orders)
print ("These are the list of sandwiches made :")
for finished_sandwich in finished_sandwiches:
	print (finished_sandwich)
		
