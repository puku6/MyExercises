class Scene(object):
	
	def __init__(self, title, urlname, description):
		self.title = title
		self.urlname = urlname
		self.description = description
		self.paths = {}
		
	def go(self, direction):
		default_direction = None
		if '*' in self.paths.keys():
			default_direction = self.paths.get('*')
		return self.paths.get(direction, None)
		
	def add_paths(self, paths):
		self.paths.update(paths)
		
#Create the scenes
		
welcome_screen = Scene("Welcome Screen", "welcome_screen", 
"""
#	def enter(self):
		# global player_name
		# global bomb_pickup
		# global bomb_placed 
		# global gorgon_1
		# global gothon_2 
Greetings human! It looks like the situation you're in 
is rather miserable at the moment.... seems like 
your space ship has been invaded by a bunch of Gothons.
Well, that's pretty unfortunate, because they are not
the kind of guys you wanna invite over for a nice little
tea party. In fact the prefer more deadly activities, 
like extinguishing entire Species or shooting
cute little puppies.
So i would strongly recommend that you go find the escape pod 
in here and abandon ship ASAP, Kaito! Wait - What?
You say you aren't Kaito Momota, Luminary of the stars?"
So what is your name then?

#%s... 
Well, that name is... let's say interesting..
But anyway, you should get going now! What? You're asking who i am?
Well i suggest that instead of worrying about me you should focus
dying for the moment, so bye'onara!
# """) #% player_name
		# bomb_pickup = False
		# bomb_placed = False
		# gorgon_1 = False
		# gothon_2 = False
		# return 'central_corridor' 		
		
central_corridor = Scene ("Central Corridor", "central_corridor",
"""
# global gorgon_1
# if gorgon_1 == False:
You head off into the direction where you reckon
the escape pod could be. You rush down a big gritty
corridor and suddenly walk into a fat and slightly smelly Gothon.
What are you going to do?
1. Try some small talk
2. Tell a short joke
3. Sucker punch that douche!

# choice = raw_input(prompt)
	# if choice == '1':
After saying about five long sentences in a row
to introduce yourself, the Gothon looses it and slaps your head off
while grunting '20 Words or less!'

# return 'death'
# elif choice == '2':
You tell the Gothon a joke. After a few awkward
seconds of silence he replies with a single
loud noise which you interprete as a laugh. After that he steps
aside, grunting 'You funny. Me likes you.'
Nodding approvingly, you move down the Corridor.
# gorgon_1 = True
# return 'central_corridor'
#elif choice == '3':
Before you could move your fist even 2 inches towards him he
tears off your arm and stuffs it down your Throat.
You seem to be suprisingly dead after that.
#return 'death'
#else:
#Wrong Input; please try again"
#return 'central_corridor'
#else:
At the end of the corridor you see 3 doors.
Above each door you see a metal badge: 
1.'Laser Weapon Armory'
2.'Bridge'
3. Escapepods
Which one do you take?

#print "Central Corridor, 3 Doors, LWA, BRIDGE, ESCPOD"
	#cc_choice = raw_input(prompt)
	#if cc_choice == '1':
	#	return 'laser_armory'
	#elif cc_choice == '2':
	#	return 'bridge'
	#elif cc_choice == '3':
	#	return 'escapepod'
	#else:
	#	self.inperror()
""")
		
laser_armory = Scene ("Laser Armory", "laser_armory", 
"""

#global bomb_pickup
#if bomb_pickup == False:
#	counter = 0
You enter a room which seems to be some kind
Of armory. You find a neutron bomb which you could use
to blow up the ship right before escaping it,
but it's locked away inside an iron box."

The box has a keypad with the numbers 1,2 and 3
which you have to enter in a specific number.
Each number can only be entered once.
Enter it in format X-X-X
	#choice = raw_input(prompt)
	#if choice == '3-1-2':
You hear a 'click' and the metal box opens.
Carefully you pick up the small, white ball inside
and hide it in your pocket and leave the armory.
		#bomb_pickup = True
		#return 'central_corridor'
#	elif choice != '3-1-2':
	#	counter + 1
The metal box beeps in a intimidating way."
But it seems that you have 10 tries."
So you have 9 left."
		#choice = raw_input(prompt)
		#while (choice != '3-1-2') and (counter < 9) :
			#counter += 1
The metal box beeps in an intimidating way."
Seems like it was the wrong number again. Try again."
			#choice = raw_input(prompt)
			 #%s" % counter
			#if choice == '3-1-2':
You hear a 'click' and the metal box opens."
Carefully you pick up the small, white ball inside"
and hide it in your pocket and leave the armory.\n"
#bomb_pickup = True
				#return 'central_corridor'
			#elif counter == 9 :
Seriously? It's only 3 numbers! You die of stupidity! "
				#return 'death'
#if bomb_pickup == True:
You already have the bomb. You should check out the other rooms.
		#return 'central_corridor'
		#if choice == 'Yes':
	#		bomb_pickup = True
	#		return 'central_corridor'
	#	elif choice == 'No':
	#		return 'central_corridor'
	#	else:
		#		print "Wrong Input; please try again"
		#		return 'laser_armory'
		#else:
		#	print "bomb is gone; return to CentralCorridor"
		#	return 'central_corridor'
""")
the_bridge = Scene ("The Bridge", "the_bridge", 
"""
	# def enter(self):
		# global bomb_pickup
		# global bomb_placed
		# global gothon_2
		# if gothon_2 == False:
You enter the middle door and notice that the room behind"
is the bridge of the ship. You notice too late that there"
is another Gothon in this room so you have to face him. "
What do you do?"
 1. Sing a lullaby"
 2. Tell him that he has beautiful eyes"
 3. Insult his morther"
choice = raw_input(prompt)
#if choice == '1':
 You start singing a lullaby and soon after that you notice"
 that the Gothon looks very sleepy."
 As soon as he starts snoring you pass him and go to the terminal."
#gothon_2 = True
#return 'bridge'
	
#elif choice == '2': 
 You tell the Gothon that his eyes look brigther"
 than all the stars in the universe. But for some reason"
 he doesn't seem very flustered. Instead"
 He vomits all over you. The caustic substance corrodes"
 your entire body into a smelly little puddle of gunk."
#				return 'death'
			
#elif choice == '3': 
 You tell the Gothon that his mother is so fat, that she is on"
 both sides of the family. After he has processed what you just"
 said, he grabs your head and pulls it off alongside your spine."
 Just before you die you hear a deep voice murmuring 'FATALITY!'"
#return 'death'
#else:
 Wrong Input; please try again"
#return 'bridge'
#elif gothon_2 == True:
 You stand infront of the beeping Terminal. "
#if bomb_placed == False and bomb_pickup == True:
 You take the Bomb out of your Pocket and place it on the Terminal."
 You activate the Timer and run out of the room."
#bomb_placed = True
#return 'central_corridor'
#elif bomb_placed == True:
 You dont have the time to check the Bridge! You should get out of here!"
#return 'central_corridor'
#elif bomb_pickup == False:
 You can't do anything here. Maybe you have missed an Item?" 
 You go back into the central corridor."
#return 'central_corridor'
""")	
		
escape_pod = Scene ("Escape Pod", "escape_pod", 
"""
# def enter(self):
# global bomb_placed
 As you enter the right room, the first thing you see are the escape pods.
 Unfortunately your happines about findingt it so easily is dulled a little by 
 the fact that there are apparently three of them.
 You remember vaguely that only one of them is actually working.
 Which one do you take?
 """)
#choice = int(raw_input(prompt))
#pod = randint(1,3)
#if choice == pod and bomb_placed == True:
the_end_winner = Scene ("You made it!", "the_end_winner", 
"""
 Whoohoo, you did it! You mate it our alive! But while you  are watching"
 your fireworks in the sky, you can't stop wondering who the hell that voice was "
 which helped you figure out your plan..."
#return 'retry'
#elif choice != pod and bomb_placed == True:
# %d" % pod
""")
the_end_loser = Scene ("...", "the_end_loser", 
"""
 You try to start the pod, but the engine won't fire."
 You explode alongside a pretty sound and light"
 provided by your own bomb."
 Well, at least you killed the Gothons."
 """)
#return 'death'
			
#elif bomb_placed == False:
 #'It worked' Thats what you thought right after arriving at the planet you escaped to."
 #And just before the Gothons blow you up alongside that entire planet."
 #Bad thing that planet had to be demolished for a galactic freeway."
#return 'death'
#else:
 #As you stay there, trying to decide which pod you take"
 #your bomb goes off and you explode alongside your ship."
 #You should've just picked one of the numbers."
#return 'death'
#""")

generic_death = Scene ("Death...", "death", "U dead.")

# class Death(Scene):

	# def enter(self):
		# print "U dead." 
		# print "Try Again?"
		# try_again = raw_input('Yes/No > ')
		# if try_again == 'Yes':
			# return 'welcome_screen'
		# else:
			# quit()		
	
# class InputError(Scene):
	
	# def enter(self):
		# print "Wrong Input; please try again"
		# return scene_name
		
# class Retry(Scene):	
	# def enter(self):
		# print "wanna start again?"
		# choice = raw_input(prompt)
		# if choice == 'Yes':
			# return 'welcome_screen'
		# else:
			# quit
generic_death = Scene("Death...", "death", "You died.") 
# Define the action commands available in each scene 
escape_pod.add_paths({
	'2': the_end_winner,
	'*': the_end_loser
})

the_bridge.add_paths({
	'throw the bomb': generic_death,
	'slowly place the bomb': escape_pod
})

escape_pod.add_paths({
	'3-1-2': the_bridge,
	'*': generic_death
})

escape_pod.add_paths({
	'shoot!': generic_death,
	'dodge!': generic_death,
	'tell a joke': laser_armory
})
		
SCENES = {
	welcome_screen.urlname: welcome_screen,
	central_corridor.urlname : central_corridor,
	laser_armory.urlname : laser_armory,
	the_bridge.urlname : the_bridge,
	escape_pod.urlname : escape_pod,
	the_end_winner.urlname : the_end_winner,
	the_end_loser.urlname : the_end_loser,
	generic_death.urlname : generic_death
}
START = central_corridor

	#'input_error': InputError(),
	#'retry': Retry()}	
	# def __init__(self, start_scene):
		# print "Start map; scene %s" %start_scene
		# self.start_scene = start_scene
		# print "start scene is %s" %start_scene
		# welcome_screen = WelcomeScreen()
		# print "end of init map" 
		
	# def next_scene(self, scene_name):
		# #print "next scene"
		# #print "current scene name %s" % scene_name
		# scene_dict = self.scenes[scene_name]
		# #print "dict scene is %s" %scene_dict
		# return scene_dict

		# print "now status scene_map"
		# ##print "start scene? %s" %scene_name
		# return scene_name

	# def opening_scene(self):
		# Map.start_scene = opening_scene
		# print "b %r" % opening_scene
		# current_scene.enter()
		

		
# a_map = Map('welcome_screen')
# #print "c %r" % a_map
# a_game = Engine(a_map)
# #print "d %r" %a_game
# a_game.play()
# #print "end"
