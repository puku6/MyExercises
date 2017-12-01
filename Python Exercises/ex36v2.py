from sys import exit

prompt = "> "
global screwdiver_Inventory
global puppy_sleep
global screwdiver_ground
def start():
	global screwdiver_Inventory
	global puppy_sleep
	global screwdiver_ground
	screwdiver_Inventory = False
	puppy_sleep = False
	screwdiver_ground = False
	print "Your adventure beginds."
	print "You stand infront of a dungeon."
	print "What do you do?"
	
	choice = raw_input(prompt)
	
	if "enter" in choice or "Enter" in choice:
		entrance()
	else:
		print "You don't enter the dungeon. "
		print "Your adventure ends."
		print "You are so boring. Slowpoke."
		retry()
		
def retry():
	print "Do you want to start again?"
	retry_answ = raw_input(prompt)
	
	if retry_answ == "yes":
		start()
	else:
		exit(0)
	
	
	
def entrance():
	print "The entrance is a dark, dusty hall."
	print "The Wall is engraved with the number 6."
	print "There is a door. What do you do?"
	door_1 = raw_input(prompt)
	
	print "Before you can do anything..."
	print "...a trap door opens beneath you."
	print "You fall into darkness."
	print "With a blunt noise you hit the ground."
	print "What do you look for?"
	choice_2 = raw_input(prompt)
	
	if ("fire" in choice_2 or "light" in choice_2
	or 	"Fire" in choice_2 or "Light" in choice_2):
		fire_yes()
	else:
		print "You stumble around in the darkness..."
		print "... until you hit your pinky toe."
		print "You die of pain."
		retry()
def fire_yes():
	print "You find a firefly called Peter." 
	print "He kindly offers to help you."
	print "You eat him."
	print "Now you illuminate a faint light."
	print "You can see now that..."
	entrance_light()	
def entrance_light():

	print "Infront of you are three doors."
	print "The left one looks like a little cat."
	print "The middle one looks like cute penguin."
	print "The right one looks like a tiny puppy."
	print "Which one do you enter?"
	door_2 = raw_input(prompt)
		
	if ("left" in door_2 or "Left" in door_2 or
		"Cat" in door_2 or "cat" in door_2) :
		room_man()
		
	elif ("right"  in door_2 or "Right" in door_2 
	or "dog" in door_2 or "Dog" in door_2 or "puppy"
	in door_2 or "Puppy" in door_2) :
		room_dog()
	elif ("middle" in door_2 or "Middle" in door_2
	or "penguin" in door_2 or "Penguin" in door_2 in door_2) :
		room_question()
	else:
		input_error()
		
def room_dog():
	global screwdiver_Inventory
	global puppy_sleep
	global screwdiver_ground
	if  puppy_sleep == False:
		print "Infront of you sits a small puppy."
		print "In his mouth is weird looking item."
		print "What do you do?"
		puppy_1 = raw_input(prompt)
	
		if "pet" in puppy_1 or "pet" in puppy_1: 
			print "You pet the puppy."
			print "The puppy enjoys it so much, that he drops the item and falls asleep."
			puppy_sleep = True
			screwdiver_ground = True
			room_dog()
		elif "hurt" in puppy_1 or "kill" in puppy_1 or "attack" in puppy_1:
			hurt_puppy()
		elif "leave" in puppy_1 or "Leave" in puppy_1:
			entrance_light() 
		else:
			input_error()
		
	elif (puppy_sleep == True and screwdiver_ground == True):
		print "Infront of you sleeps a small puppy."
		print "Next to it lies a weird looking item."
		print "What do you do?"
		puppy_2 = raw_input(prompt)
		if ("pick up" in puppy_2 or "get" in puppy_2 
		or "take" in puppy_2 or "Take" in puppy_2): 
			print "You pick up the item. It's a weird looking screwdiver."
			screwdiver_ground = False
			screwdiver_Inventory = True
			room_dog()
		elif "hurt" in puppy_2 or "kill" in puppy_2 or "attack" in puppy_2:
			hurt_puppy()
		elif "leave" in puppy_2 or "Leave" in puppy_2:
			entrance_light() 
		else:
			input_error()
	else: 
		print "Infront of you sleeps a small puppy."
		print "What do you do?"
		puppy_3 = raw_input(prompt)
		if "hurt" in puppy_3 or "kill" in puppy_3 or "attack" in puppy_3:
			hurt_puppy()
		elif "leave" in puppy_3 or "Leave" in puppy_3:
			entrance_light() 
		else:
			input_error()


def hurt_puppy():
		print "You kill the puppy."
		print "It was very easy."
		print "You cruel human being."
		print "You die of shame."
		retry()		


def room_man():
	print "In the room stands an old man."
	print "He looks nice."
	print "'Hey there my child,' he says in creaky voice."
	print "'Are you in need of some chocolate?'"
	print "What do you answer?"
	man_answer = raw_input(prompt)
	
	if "Yes" in man_answer or "yes" in man_answer or "Hell yeah!" in man_answer:
		print "He gives you a tasty and nutricious looking bar of chocolate."
		print "Then he shoots you."
		print "As you lie on the ground, dying..."
		print "He approaches your ear and whispers..."
		print "'Didnt your Mom teach you:..."
		print "'...Never take candy from a stranger.'"
		retry()
	if "no" in man_answer or "No" in man_answer or "Hell no!" in man_answer:
		print "'Fine!' he shouts. 'Then leave or i shall smite thee!'"
		entrance_light()
		
def input_error():
	print "Odin appears infront of you."
	print "'You know nothing, Jon Snow!' he says."
	print "He slaps you with his backhand."
	print "You die. Painfully."
	retry()

def room_question():
	print "You enter a room with a bridge."
	print "The door falls shut behind you."
	print "It is locked."
	print ""
	print "On the bridge stands a crazy looking old man."
	print "In a thunderin voice he yells:..."
	print "'STOP! Who would cross the bridge of death.."
	print "'Must answer meeee this questions three...'"
	print "'...before the other side he sees."
	print "WHAT is your name?"
	name = raw_input(prompt)
	
	if name == "Kevin":
		print "'KEVIN???I DON'T LIKE THIS NAME!'"
		print "'I DON'T LIKE THIS NAME!!'"
		bridge_death()
	else:
		print "'CORRECT! So tell me, %s...'" % name
		print "'What is the Answer to the...'"
		print "'Ultimate Question of Life, The Universe, and Everything?'" 
		answer_42 = raw_input(prompt)
		if answer_42 == "42":
			print "'CORRECT! So, the last question...'"
			print "'Which number is engraved into the Wall in the Entrance?"
			answer_6 = raw_input(prompt) 
			if answer_6 == "6": 
				print "AGAIN, CORRECT!" 
				print "You may pass!"
				room_baal()
			else:
				bridge_death()
		else:
				bridge_death()

def bridge_death():
	print "He shoves you and you fall down."
	print "You fall. And fall. And fall."
	print "Forever. Until you die of starvation."
	retry()

def room_baal():
	global screwdiver_Inventory 
	print "You pass the bridge."
	print "On the other side is a door to an elevator."
	print "You enter. There is only one button to press. Down."
	button = raw_input(prompt)
	if "press" in button or "Press" in button:
		print "You descend. After one hour, 42 minutes and 3 seconds the elevator stops."
		print "The door opens and you enter a room."
		print "The room is full of fire and you hear screaming."
		print "Infront of you stands a giant Humanoid with goat legs."
		print "He shouts: 'I am the almighty Baal, Ruler of the seven Hells of Death!'"
		print "'You entered my domain without permission! Now you shall DIE!'"
		baal_die=raw_input("Die! ")
		if ("Screwdriver" in baal_die or "screwdriver" in baal_die) and screwdiver_Inventory == True:
			print "You show Baal the Screwdiver."
			print "He scream: 'OH NO! HE GOT A SONIC-SCREWDRIVER!"
			print "Please don't kill me! I will even call you my master!"
			print "Congratulations. Now you are the new Master of the Seven hells."
			retry() 
		else:
			print "He touches you and you burn to cinders."
			print "You die a horrible death."
			retry() 
	else:
		input_error()
start()