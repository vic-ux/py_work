def make_shirt():
	"""summarise the size of a shirt with a catchy text for advertisment"""
	size = input('Enter your shirt size? ')
	if size == 'large' or size == 'medium':
		print ("shirt is " + size.title() + " sized, and has the following text imprint on it: I love python")
	else:
		print ("shirt is " + size.title() + " sized, and has the following text imprint on it: consistency is key")
		
make_shirt()

def make_shirt(size = 'large',text = 'I love python'):
	""" defining a default argument"""
	print("The shirt is " + size + " sized, with " + text.title() + " text.")
make_shirt(size='medium')
make_shirt(size = 'small',text= 'be yourself')

	
	

