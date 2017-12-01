print "You enter a dark room with two doors. Do you go through door #1 or door#2?"

door = raw_input("> ")

if door == "1":
	print "There's a giant bear here eating a cheese cake. What do you do?"
	print "1. Take the cake."
	print "2. Scream at the bear."
	
	bear = raw_input("> ")
	
	if bear == "1":
		print "The bear eats your face off. Good job!"
	elif bear == "2":
		print "The bear eats your arms off. Good job!"
		print "What do you do now?"
		print "1. Die in a poodle of blood, screaming 'moommyyyy!'"
		print "2. Try to run into safety."
		
		bear2 = raw_input("> ")
		
		if bear2 == "'Tis but a scratch!": 
			print "The bear eats one of your legs off. Are you happy now?"
			
			bear3 = raw_input("> ")
			if bear3 == "It's just a flesh wound!":
				print "The bear eats your other leg off, looking mildly annoyed."
				
				bear4 = raw_input("> ")
				if bear4 == "I'm invincible!":
					print "Okay, we call it a draw. Are you happy now?"
				else :
					print "After giving a good fight, you die. Finally. Not a good job, but what's done is done."
			else: 
				print "Now you're dead. Good job!"
		else:
			print "You die. Good job!"
	else: 
		print "Well, doing %s is probably better. Bear runs away." % bear
		
elif door == "2": 
	print "You stare into the endless abyss at Cthulhu's retina."
	print "1. Blueberries."
	print "2. Yellow jacket clothespins."
	print "3. Understanding revolvers yelling melodies."
	
	insanity = raw_input("> ")
	
	if insanity == "1" or insanity == "2":
		print "Your body survives powered by a mind of jello. Good job!"
	else:
		print "The insanity rots your eyes into a pool of muck. Good job!"
		
		
else:
	print "You stumble around and fall on a knife and die. Good job!"