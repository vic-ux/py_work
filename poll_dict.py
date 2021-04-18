favourite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'ade': 'java',
    'ebun': 'css',
    }

poll_list = ['ade','vic','ebun']
for key in favourite_language.keys():
	if key in poll_list:
		print('\n' + 'Thank you, '+ key.title() + ' for taking the poll.')
	else:
		print ('\n' +key.title() +', please take the poll.')
