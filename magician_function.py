def show_magician(magicians):
	""" Make a list of magicians and pass
	    them as list to a function"""
	
	for magician in magicians:
		msg = magician.title()
		print( '\n' + msg)	

def make_great(magicians):
	while magicians:
		for magician in magicians:
			print (magician.title() + ' the Great!')
magicians = ['ade','victor','ebun','lola','layo','bimbo']
greatmagician = []

show_magician(magicians)


