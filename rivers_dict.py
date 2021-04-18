rivers = {}
rivers['nile'] = 'egypt'
rivers['niger'] = 'nigeria'
rivers['congo'] = 'congo'
print (rivers)
for river,country in rivers.items():
	print('The ' + river.title() + ' runs through ' + country.title() + '.')
for key in rivers.keys():
	print('\n'+key.title())
for v in rivers.values():
	print ('\n'+v.title())
