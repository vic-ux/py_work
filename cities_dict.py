cities = {
    'ibadan':{
    'state' : 'oyo state',
    'population': 'over 11 million people.',
    'facts':'oldest city in the western region of Nigeria.',
    },  
    'abuja':{
    'state' : 'federal capital teritory',
    'population': 'over 1 million people.',
    'facts':'it is the present F.C.T of Nigeria.',
    },
    'ikeja':{
    'state' : 'lagos state',
    'population': 'over 20 million people.',
    'facts':'it the former F.C.T for Nigeria.',
    }
    }
print (cities)
for city,value in cities.items():
	print ('\n'+ 'Let talk about '+ city.title())
	for key,values in value.items():
		print ('\t' + key.title()+ ': '+ values)
		
	
		
