users = {}
 
active = True
while active:
	name = input("what is your name? ")
	question = input("if you could visit one place in the world, where would it be? " )
	 
	 
	users[name] = question
	
	repeat = input ("Do yo want anybody to give their opinion?  yes/no ")
	if repeat == 'no':
		active = False
print ("---- Polling Result ----")
for name,question in users.items():
		print (name + ", would definitely love to visit " + question + ".")
	 
