sandwich_order = []
sandwich_order.append('tuna')
sandwich_order.append('beef')
sandwich_order.append('pastrami')
sandwich_order.append('chicken')
sandwich_order.append('pastrami')
sandwich_order.append('fish')
sandwich_order.append('cheese')
print(sandwich_order)

while 'pastrami' in sandwich_order:
	sandwich_order.remove('pastrami')
print(sandwich_order)


