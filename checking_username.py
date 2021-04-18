names = ['adex','seun','nick','VIC','Bim','admin','nut']
name = ['vic','dayo','nick','tim','bim']
for i in name:
	if i.title() in names or i.upper() in names or i.lower() in names:
		print (i+' You will need to enter a new username.')
	else:
		print(i + ' is available.')
