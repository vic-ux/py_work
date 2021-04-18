
multiples = input (("input a number,let our prog. tell us if its a multiple of 10:"))
multiples = int(multiples)
if multiples > 10:
	print ('Out of range')
    
else:
	if 10 % multiples == 0:
		print('it is a multiple of 10.' )
	else:
		print ('it is not a multiple of 10.')
