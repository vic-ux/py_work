def city_country (city,country):
	""" write a neat formatted """
	name = city + ", " + country 
	return name
	
full_name = city_country('Ibadan' , 'Oyo')
print(full_name)

full_name = city_country('Ado' , 'Ekiti')
print('\n' + full_name)

full_name = city_country('Ikeja' , 'Lagos')
print('\n'  + full_name)

full_name = city_country('Oshogbo' , 'Osun')
print('\n' + full_name)
