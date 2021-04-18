game =""
started = False
while True:
	game = input(">")
	if game == "start":
		if started:
			print ("Car already started!")
		else:
			started = True
			print ("Car started...")
	elif game == "stop":
		if not started :
			print ("Car is already stopped!")
		else:
			started = False
			print("Car stopped.")
		
	elif game == "help":
		print("""
start - to start the car
stop - to stop a car
quit - to exit""")
	elif game == "quit":
		break
	else:
		print ("Sorry, I don't understand that...")
