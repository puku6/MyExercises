#dictionary damit go erkennt, ob man eine flag vor sich hat
FLAGS_Command= ['deeebug', "'deeebug'", 'tell a joke', 'take debug']
FLAGS_alt= {'take debug': 'central_corridor',
'take debug2': 'laser_weapon_armory'}
inventory= []
rooms_alt= {'central_corridor': 'central_corridoralt'}
class Scene(object):
	
	def __init__(self, title, urlname, description):
		self.title = title
		self.urlname = urlname
		self.description = description
		self.paths = {}
		self.flags = {}
	def go(self, direction):
		default_direction = None
		#inventory clear wenn neues spiel gestartet wird
		if self.urlname == 'welcome_screen':
			del inventory[:]
		#falls die kommando in den flag commandos ist, soll inventar geaendert werden
		if direction in FLAGS_Command:
			inventory.append(direction)
			print 'append inventory'
			print inventory
		if '*' in self.paths.keys():
			default_direction = self.paths.get('*')
		#falls kommando + raum kombo in flags ist, soll alternativer raum geladen werden
		if direction in FLAGS_alt and FLAGS_alt[direction] == self.urlname :
			direction += 'alt'
		return self.paths.get(direction, default_direction)
		
	def add_paths(self, paths):
		self.paths.update(paths) 

	
	
central_corridor = Scene("Central Corridor", "central_corridor", 
""" 
The Gothons of Planet Percal #25 have invaded your ship and destroyed your entire crew.
 You are the last surviving member (oh noes!) and your last mission is to get the neutron 
destruct bomb from the Weapons Armory, put it in the bridge, and blow up the ship after 
getting into an escape pod. 

You're now running down the central corridor to the Weapons 
Armory when a Gothon hops out in an evil clown costume filled with hate. 
He's blocking the door to the Armory and about to pull a weapon to blast you. 
""") #% self.FLAGS 		
#Debug Flag Status: %s
		
welcome_screen = Scene("Welcome Screen", "welcome_screen", 
"""
Greetings human! It looks like the situation you're in 
is rather miserable at the moment.... seems like 
your space ship has been invaded by a bunch of Gothons.
Well, that's pretty unfortunate, because they are not
the kind of guys you wanna invite over for a nice little
tea party. In fact the prefer more deadly activities, 
like extinguishing entire Species or shooting
cute little puppies.
So i would strongly recommend that you go find the escape pod 
in here and abandon ship ASAP!
""")
		

central_corridor_debug = Scene("Central Corridor Debug", "central_corridor_debug", 
""" 
Debug The Gothons of Planet Percal #25 have invaded your ship and destroyed your entire crew.
 You are the last surviving member (oh noes!) and your last mission is to get the neutron 
destruct bomb from the Weapons Armory, put it in the bridge, and blow up the ship after 
getting into an escape pod. 

You're now running down the central corridor to the Weapons 
Armory when a Gothon hops out in an evil clown costume filled with hate. 
He's blocking the door to the Armory and about to pull a weapon to blast you. 
Debug Flag Status: %s
""") #self.FLAGS  ) 

laser_weapon_armory = Scene("Laser Weapon Armory", "laser_weapon_armory", 
""" 
Lucky for you they made you learn Gothon insults in the academy.
 You tell the one Gothon joke you know: 
Lbhe zbgure vg fb sng, jura fur vfvg nebhaq gut ubhfr, fur fvgf nebhaq gut ubhfr. 
The Gothon bursts into laughter and rolls around on the ground. While its laughing you run up and use your copy of Nietzsche's notebooks 
(translated into Gothon) to lecture the Gothon on the shaky foundations of its ideologies.
 While it tries to cope with its existential crisis, you leap through the Weapon Armory door.
 You dive roll into the Weapon Armory, crouch and scan the room for more Gothons that might be hiding. 
It's dead quiet, too quiet. You stand up and run to the far side of the room and find the neutron bomb in its container. 
There's a keypad lock on the box and you need the code to get the bomb out. 
If you get the code wrong 10 times then the lock closes forever and you can't get the bomb. The code is 3 digits. 
Debug Flag Status: %s
""") #% self.FLAGS) 

the_bridge = Scene("The Bridge", "the_bridge", 
""" 
The container clicks open and the seal breaks, letting gas out. You grab the 
neutron bomb and run like heck to the bridge where you place it in the right spot. 
You burst into the Bridge with the bomb under your arm and surprise 5 Gothons
 who are trying to take control of the ship. Each of them has an uglier clown 
costume that the last. They don't pull their weapons out of fear that they will 
set off the bomb under your arm. 
""") 

escape_pod = Scene("Escape Pod", "escape_pod",
""" 
You gesture towards the bomb and threaten to set it off, the Gothons put up 
their arms and ask for a truce. You inch backwards to the door, open it, and 
carefully place the bomb on the floor, waving your finger over the detonate button.
Then you jump back through the door, hit the close button and zap the lock so they can't get out.
 Now that the bomb is placed you run to the escape pod. 
You rush through the ship desperately trying to make it to the escape pod. 
It seems like there's no Gothons around, so you run as fast as possible. 
Eventually you reach the room with the escape pods, and you now need to pick one to take. 
Some of them could be damaged, but you don't have time to look. There's 5 pods, which one do you take? 
""") 

the_end_winner = Scene("You Made It!", "the_end_winner", 
""" 
You jump into pod 2 and hit the eject button. The pod flies out into
 space heading to the planet below. As you're heading down, you look back and see your ship
 implode and then explode like a supernova, taking down the Gothon ship at the same time. You made it! 
""") 

the_end_loser = Scene("...", "the_end_loser",
 """
 You jump into a random pod and hit the eject button. 
The pod escapes into space but there's a crack in the hull. Uh oh. 
The pod implodes and you with it. 
""") 

generic_death = Scene("Death...", "death", "You died.")

#welcome screen transition zu central corridor: html muss noch geaendert werden!
welcome_screen.add_paths({
	'*': central_corridor
})
	
escape_pod.add_paths({
	'2': the_end_winner,
	'*': the_end_loser
})

the_bridge.add_paths({
	'throw the bomb': generic_death,
	'slowly place the bomb': escape_pod
})

laser_weapon_armory.add_paths({
	'3-1-2': the_bridge,
	'*': generic_death,
	'deeebug': central_corridor,
	'deeebugalt': central_corridor,
	'take debug2': central_corridor
})

escape_pod.add_paths({
	'shoot!': generic_death,
	'dodge!': generic_death,
	'tell a joke': laser_weapon_armory
})
central_corridor.add_paths({
    'shoot!':generic_death,
    'dodge!':generic_death,
    'tell a joke': laser_weapon_armory,
	'take debug': central_corridor,
	'take debugalt': central_corridor_debug
	})
	
central_corridor_debug.add_paths({
    'shoot!':generic_death,
    'dodge!':generic_death,
    'tell a joke': laser_weapon_armory,
	'debug': central_corridor
	})


SCENES = {
	welcome_screen.urlname: welcome_screen,
	central_corridor_debug.urlname : central_corridor_debug,
	central_corridor.urlname : central_corridor,
	laser_weapon_armory.urlname : laser_weapon_armory,
	the_bridge.urlname : the_bridge,
	escape_pod.urlname : escape_pod,
	the_end_winner.urlname : the_end_winner,
	the_end_loser.urlname : the_end_loser,
	generic_death.urlname : generic_death
}


	
START = welcome_screen