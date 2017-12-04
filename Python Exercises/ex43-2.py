from sys import exit 
from random import randint
prompt = "> "


class Scene(object):

	def enter(self):
		pass
		
class Engine(object):
		
		def __init__(self, scene_map):
			
			#print "status scene map %s" % scene_map
			self.scene_map = scene_map
			#print "engine init" 
			
		def play(self):
			#print "engine play start "
			
			
			scene_name = self.scene_map.start_scene
			#print "current scene name %s" %scene_name
			#print "start loop"
			while scene_name != 'end_screen':
				#print "starting scene name is %s " % scene_name
				current_scene=self.scene_map.next_scene(scene_name)
				#print "got scene_name %s" % current_scene
				scene_name = current_scene.enter()
			
				#print "restart scene loop "
			
			print "%s" % scene_name
			#start_scene(self, scene_map)
			
			#scene_map = a_map
			#a_map = Map('Welcome_Screen)
			
			#opening
			#a_game.play()
			#play(Engine(Map('Welcome_Screen')))
			#play(Engine(scene_map))
			#print "self 2 %s" % self
			
			#scene_map.opening_scene(welcome_screen)

class WelcomeScreen(Scene):
	
	def enter(self):
		global player_name
		global bomb_pickup
		global bomb_placed 
		global gorgon_1
		global gothon_2 
		print "Greetings human! It looks like the situation you're in"
		print "is rather miserable at the moment.... seems like "
		print "your space ship has been invaded by a bunch of Gothons. "
		print "Well, that's pretty unfortunate, because they are not"
		print "the kind of guys you wanna invite over for a nice little"
		print "tea party. In fact the prefer more deadly activities, "
		print "like extinguishing entire Species or shooting"
		print "cute little puppies."
		print "So i would strongly recommend that you go find the escape pod "
		print "in here and abandon ship ASAP, Kaito! Wait - What?"
		print "You say you aren't Kaito Momota, Luminary of the stars?"
		print "So what is your name then?"
		player_name = raw_input(prompt)
		print "%s... Well, that name is... let's say interesting.." % player_name
		print "But anyway, you should get going now! What? You're asking who i am?"
		print "Well i suggest that instead of worrying about me you should focus"
		print "dying for the moment, so bye'onara!"
		bomb_pickup = False
		bomb_placed = False
		gorgon_1 = False
		gothon_2 = False
		return 'central_corridor' 
		
class Death(Scene):

	def enter(self):
		print "U dead." 
		print "Try Again?"
		try_again = raw_input('Yes/No > ')
		if try_again == 'Yes':
			return 'welcome_screen'
		else:
			quit()
				
class CentralCorridor(Scene):

	def enter(self):
		global gorgon_1
		if gorgon_1 == False:
			print "You head off into the direction where you reckon"
			print "the escape pod could be. You rush down a big gritty "
			print "corridor and suddenly walk into a fat and slightly smelly Gothon. "
			print "What are you going to do?"
			print "1. Try some small talk"
			print "2. Tell a short joke"
			print "3. Sucker punch that douche!"
			choice = raw_input(prompt)
			if choice == '1':
				print "After saying about five long sentences in a row"
				print " to introduce yourself, the Gothon looses it and slaps your head off"
				print "while grunting '20 Words or less!'"
				return 'death'
			elif choice == '2':
				print "You tell the Gothon a joke. After a few awkward"
				print "seconds of silence he replies with a single"
				print "loud noise which you interprete as a laugh. After that he steps"
				print "aside, grunting 'You funny. Me likes you.'"
				print "Nodding approvingly, you move down the Corridor."
				gorgon_1 = True
				return 'central_corridor'
			elif choice == '3':
				print "Before you could move your fist even 2 inches towards him he"
				print "tears off your arm and stuffs it down your Throat."
				print "You seem to be suprisingly dead after that."
				return 'death'
			else:
				print "Wrong Input; please try again"
				return 'central_corridor'
		else:
			print "At the end of the corridor you see 3 doors."
			print "Above each door you see a metal badge: "
			print "1.'Laser Weapon Armory'"
			print "2.'Bridge'"
			print "3. Escapepods"
			print "Which one do you take?"
		#print "Central Corridor, 3 Doors, LWA, BRIDGE, ESCPOD"
			cc_choice = raw_input(prompt)
			if cc_choice == '1':
				return 'laser_armory'
			elif cc_choice == '2':
				return 'bridge'
			elif cc_choice == '3':
				return 'escapepod'
			else:
				print "Wrong Input; please try again"
				return 'central_corridor'
		
class LaserWeaponArmory(Scene):

	def enter(self):
		global bomb_pickup
		if bomb_pickup == False:
			counter = 0
			print "You enter a room which seems to be some kind"
			print "Of armory. You find a neutron bomb which you could use"
			print "to blow up the ship right before escaping it,"
			print "but it's locked away inside an iron box."
			print "The box has a keypad with the numbers 1,2 and 3"
			print "which you have to enter in a specific number."
			print "Each number can only be entered once."
			print "Enter it in format X-X-X"
			choice = raw_input(prompt)
			if choice == '3-1-2':
				print "You hear a 'click' and the metal box opens."
				print "Carefully you pick up the small, white ball inside"
				print "and hide it in your pocket and leave the armory."
				bomb_pickup = True
				return 'central_corridor'
			elif choice != '3-1-2':
				counter + 1
				print "The metal box beeps in a intimidating way."
				print "But it seems that you have 10 tries."
				print "So you have 9 left."
				choice = raw_input(prompt)
				while (choice != '3-1-2') and (counter < 9) :
					counter += 1
					print "The metal box beeps in an intimidating way."
					print "Seems like it was the wrong number again. Try again."
					choice = raw_input(prompt)
					print "%s" % counter
					if choice == '3-1-2':
						print "You hear a 'click' and the metal box opens."
						print "Carefully you pick up the small, white ball inside"
						print "and hide it in your pocket and leave the armory.\n"
						bomb_pickup = True
						return 'central_corridor'
					elif counter == 9 :
						print "Seriously? It's only 3 numbers! You die of stupidity! "
						return 'death'
		if bomb_pickup == True:
				print "You already have the bomb. You should check out the other rooms."
				return 'central_corridor'

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
class TheBridge(Scene):

	def enter(self):
		global bomb_pickup
		global bomb_placed
		global gothon_2
		if gothon_2 == False:
			print "You enter the middle door and notice that the room behind"
			print "is the bridge of the ship. You notice too late that there"
			print "is another Gothon in this room so you have to face him. "
			print "What do you do?"
			print "1. Sing a lullaby"
			print "2. Tell him that he has beautiful eyes"
			print "3. Insult his morther"
			choice = raw_input(prompt)
			if choice == '1':
				print "You start singing a lullaby and soon after that you notice"
				print "that the Gothon looks very sleepy."
				print "As soon as he starts snoring you pass him and go to the terminal."
				gothon_2 = True
				return 'bridge'
				
			elif choice == '2': 
				print "You tell the Gothon that his eyes look brigther"
				print " than all the stars in the universe. But for some reason"
				print "he doesn't seem very flustered. Instead"
				print "He vomits all over you. The caustic substance corrodes"
				print "your entire body into a smelly little puddle of gunk."
				return 'death'
			
			elif choice == '3': 
				print "You tell the Gothon that his mother is so fat, that she is on"
				print "both sides of the family. After he has processed what you just"
				print "said, he grabs your head and pulls it off alongside your spine."
				print "Just before you die you hear a deep voice murmuring 'FATALITY!'"
				return 'death'
			else:
				print "Wrong Input; please try again"
				return 'bridge'
		elif gothon_2 == True:
			print "You stand infront of the beeping Terminal. "
			if bomb_placed == False and bomb_pickup == True:
				print "You take the Bomb out of your Pocket and place it on the Terminal."
				print "You activate the Timer and run out of the room."
				bomb_placed = True
				return 'central_corridor'
			elif bomb_placed == True:
				print "You dont have the time to check the Bridge! You should get out of here!"
				return 'central_corridor'
			elif bomb_pickup == False:
				print "You can't do anything here. Maybe you have missed an Item?" 
				print "You go back into the central corridor."
				return 'central_corridor'
	
		
class EscapePod(Scene):

	def enter(self):
		global bomb_placed
		print "As you enter the right room, the first thing you see are the escape pods."
		print "Unfortunately your happines about findingt it so easily is dulled a little by "
		print "the fact that there are apparently three of them."
		print "You remember vaguely that only one of them is actually working."
		print "Which one do you take?"
		choice = int(raw_input(prompt))
		pod = randint(1,3)
		if choice == pod and bomb_placed == True:
			print "Whoohoo, you did it! You mate it our alive! But while you  are watching"
			print "your fireworks in the sky, you can't stop wondering who the hell that voice was "
			print "which helped you figure out your plan..."
			return 'retry'
		elif choice != pod and bomb_placed == True:
			print "%d" % pod
			print "You try to start the pod, but the engine won't fire."
			print "You explode alongside a pretty sound and light"
			print "provided by your own bomb."
			print "Well, at least you killed the Gothons."
			return 'death'
			
		elif bomb_placed == False:
			print "'It worked' Thats what you thought right after arriving at the planet you escaped to."
			print "And just before the Gothons blow you up alongside that entire planet."
			print "Bad thing that planet had to be demolished for a galactic freeway."
			return 'death'
		else:
			print "As you stay there, trying to decide which pod you take"
			print "your bomb goes off and you explode alongside your ship."
			print "You should've just picked one of the numbers."
			return 'death'
		
	
class InputError(Scene):
	
	def enter(self):
		print "Wrong Input; please try again"
		return scene_name
		
class Retry(Scene):	
	def enter(self):
		print "wanna start again?"
		choice = raw_input(prompt)
		if choice == 'Yes':
			return 'welcome_screen'
		else:
			quit
class Map(object):

	scenes = {
	'welcome_screen': WelcomeScreen(),
	'central_corridor': CentralCorridor(),
	'laser_armory': LaserWeaponArmory(),
	'bridge': TheBridge(),
	'escapepod': EscapePod(),
	'death': Death(),
	'input_error': InputError(),
	'retry': Retry()}	
	def __init__(self, start_scene):
		print "Start map; scene %s" %start_scene
		self.start_scene = start_scene
		print "start scene is %s" %start_scene
		welcome_screen = WelcomeScreen()
		print "end of init map" 
		
	def next_scene(self, scene_name):
		#print "next scene"
		#print "current scene name %s" % scene_name
		scene_dict = self.scenes[scene_name]
		#print "dict scene is %s" %scene_dict
		return scene_dict

		print "now status scene_map"
		##print "start scene? %s" %scene_name
		return scene_name

	def opening_scene(self):
		Map.start_scene = opening_scene
		print "b %r" % opening_scene
		current_scene.enter()
		

		
a_map = Map('welcome_screen')
#print "c %r" % a_map
a_game = Engine(a_map)
#print "d %r" %a_game
a_game.play()
#print "end"