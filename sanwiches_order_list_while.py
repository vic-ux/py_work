sandwich_orders = []
sandwich_orders.append('beef')
sandwich_orders.append('chicken')
sandwich_orders.append('cheese')
sandwich_orders.append('fish')
sandwich_orders.append('turkey')
print (sandwich_orders)
finished_sandwiches = []
while sandwich_orders:
	sandwich_order = sandwich_orders.pop()
	
	print ("\nI made you a " + sandwich_order + " sandwich.")
finished_sandwiches.append(sandwich_order)

		
