def new_album(name,title,tracks ):
	""" function to tke in an artist name with the album title"""
	history = {}
	history['Artist Name'] = name
	history['Album Title'] = title
	if tracks:
		history['tracks'] =  tracks
	return history

while True:
	print("Enter 'q' to exit")
	name = input ('Enter artist name : ')
	if name == 'q' :
		break
	title = input ('Enter album title : ')
	if title == 'q':
		break
	tracks = input ('Enter the number of tracks in the album : ')
	if tracks == 'q':
		break
	musician = new_album(name,title,tracks )
	print (musician)






