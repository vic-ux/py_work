favourite_places = {}
favourite_places['ebun'] ='shoprite', 'ICM'
favourite_places['victor'] = 'dominos pizza', 'coldstone'
favourite_places['gbola'] = 'agodi garden', 'ventura'
print (favourite_places)
for name,place in favourite_places.items():
	print ("\n" +  name.title() + "'s favourite places are as follows: " )
	for places in place:
		print('\t' + places.title()) 




favorite_languages = {
    'jen': ['python', 'ruby'],    
    'sarah': ['c'],    
    'edward': ['ruby', 'go'],    
    'phil': ['python', 'haskell'],   
     }
print (favorite_languages)
for name, languages in favorite_languages.items():
	print("\n" + name.title() + "'s favorite languages are:")
	for language in languages:
		print("\t" + language.title())
