print "An old man comes to you and asks 'Food for a poor old man?"
print "What do you do?"
print "1. Give him a piece of sugar, because he could might be an elf or something."
print "2. Don't give him anything."

food = raw_input("> ")

if food == "1":
	print "'I'm actually not an old, I'm Magic Man! You gave me that candy,now i will do you a favor!'"
	print "He turns you into a giant foot."
	print "What do you do now?"
	print "1. Scream: 'Hey! Turn me back!'"
	print "2. Accept your life as a foot and jump into the sunset."
	
	foot = raw_input("> ")
	
	if foot == "1":
		print "Not until you appreciate what a Jerk I am!"
		print "What do you do now?"
		print "1. Accept your life as a foot and jump into the sunset."
		
		foot_2 = raw_input("> ")
		if foot_2 == "1":
			print "Your journey ends under the bridge in company of a giant Hand, a giant Eye and a toilet. "
		elif foot_2 == "You are a giant jerk, Magic man.":
			print "'You are right!' He turns you back into your true form and vanishes."
		else:
			print "You do nothing. Now you are a depressed foot."
	elif foot  == "2":
		print "Your journey ends under the bridge in company of a giant Hand, a giant Eye and a toilet. "
		
	else: 
		print "You do nothing. Now you are a depressed foot."
		
elif food == "2": 
	print "You don't give the poor, starving old man anything."
	print "Sometimes helping a starving homeless guy isn't the right thing to do."
	print "After you live a fulfilled life, you enter hell."
	print "For not helping that guy. Douche."
	
	
		
		
else:
	print "The homeless guy takes out a Knife and kills you and your husband/wife."
	print "Now your kid can become Batman. Good job."