people_number = {}
people_number['emma']= [14 , 10, 30]
people_number['vic']= [21, 10, 1]
people_number['gbola']=[ 9, 20,90]
people_number['ebun']= [20, 40, 59]
people_number['layo']= [12, 34, 56]
people_number['bimbo']= [24, 13, 47]
people_number['lola']= [18, 53, 44]
print(people_number)
for name,number in people_number.items():
	print('\n' + name.title() + "'s favourite numbers are: ")
	for numbers in number:
		
		print (numbers)


