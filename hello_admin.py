names = ['adex','seun','vic','nick','bim','admin','nut']
for name in names:
	if name == 'admin':
		print('Hello '+ name +', would you like to see a status report?')
	else:
		print('Hello '+name + ', ' + 'thank you for logging in again.')
		
		
		
		
		
if names:
	for name in names :
		print('\nwe love you')
else:
	print (' We need to find some users!')
	
names.remove('seun')
names.remove('adex')
names.remove('bim')
names.remove('nut')
names.remove('nick')
names.remove('vic')
names.remove('admin')

print(names)
if names:
	for name in names :
		print('\nwe love you')
else:
	print (' We need to find some users!')
