age = input ('How old are you? ')
age = int(age)
while  True:
	if age < 3:
		print("Ticket is free")
		break
	elif age <= 12:
		print ("Ticket is $10")
		break
	elif age > 12:
		print ('Ticket is $15')
		break
	else:
		print (age)
		
		
		 
