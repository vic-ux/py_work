def new_album(name,title,tracks = ''):
	""" function to tke in an artist name with the album title"""
	history = {}
	history['Artist Name'] = name
	history['Album Title'] = title
	if tracks:
		history['tracks'] =  tracks
	return history

musician = new_album('Burnaboy' , 'Twice as tall', tracks = 13 )
print (musician)

musician = new_album('Wizkid' , 'Ayo', 14)
print (musician)

musician = new_album('2 Face Idibia' , 'Warrior', 13 )
print (musician)




