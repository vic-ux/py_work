stages = input (str('how old are you? '))
if int(stages) < 2:
	print ('you are a baby')
elif int(stages) < 4 :
	print ('you are a toddler')
elif int(stages) < 13 :
	print ('you are a kid')
elif int(stages) < 20 :
	print ('you are a teenager')
elif int(stages) < 65 :
	print ('you are an adult')
else:
	print('you are an elder')
	

	
