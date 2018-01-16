

# command and urlname, so go can recognize, if there is an item in that scene
FLAGS_item= {
"3-1-2": ['laser_weapon_armory', 'laser_weapon_armory_box_wrong1', 'laser_weapon_armory_box_wrong2']
}
# same for events
FLAGS_events= {
"sing": 'the_bridge'
}

#self.urlname + keyword for event
event_assoc = {
'the_bridge': 'gothon',
'the_bridge_alt': 'bomb'
}
#self.urlname + item
item_assoc = {
'laser_weapon_armory':'bomb',
'laser_weapon_armory_box_wrong1':'bomb',
'laser_weapon_armory_box_wrong2':'bomb'
}
#dict for flags_set and items picked up
FLAGS_item_affectroom = {
'bomb' : 'central_corridor_alt'
}

#translation for flags_list 
FLAGS_ressource = {
'bomb laser_weapon_armory' : 'bomb pickup',
'bomb laser_weapon_armory_box_wrong1' : 'bomb pickup',
'bomb laser_weapon_armory_box_wrong2' : 'bomb pickup',
'bomb the_bridge_alt' : 'bomb placed',
'gothon the_bridge': 'gothon asleep'}

#rooms which will be affected by the triggered flag
FLAGS_flag_affectroom = {
'bomb pickup' : ['central_corridor_alt'],
'gothon asleep': ['central_corridor_alt'],
'bomb placed': ['central_corridor_alt', 'escape_pod']}
 
#dict for the flags which affect a room
FLAGS_alt = {
'central_corridor_alt': ['gothon asleep', 'bomb placed', 'bomb pickup'],
'escape_pod': ['bomb placed']
}

#item requirement
item_req = {
'place bomb': 'bomb'}

#directions that should lead to alternative rooms, if a flag is set
FLAG_flag_affectdir = {
'bomb pickup' : ['lwa'],
'gothon asleep' : ['bridge'],
'bomb placed': ['bridge', '2', '1', '3']
 }

#memory for inventory
inventory= []

#memoryr for triggered flags
FLAGS_list= []

class Scene(object):

	def __init__(self, title, urlname, description):
		self.title = title
		self.urlname = urlname
		self.description = description
		self.paths = {}
		self.flags = {}
	def go(self, direction):
		default_direction = None
		#inventory and flags clear if new game is started
		if self.urlname == 'welcome_screen':
			del inventory[:]
			del FLAGS_list[:]
		#if there is a flag affecting the direction, an alternative direction should be chosen
		flag_source = " ".join([direction, self.urlname])
		for x in FLAGS_alt.get(self.urlname, 'error'):
			flag_all = " ".join([flag_source, x])
			if flag_all in FLAGS_list:
				direction += 'alt'
				break
		
		#see if there is an item in that room 	
		if direction in FLAGS_item and self.urlname in FLAGS_item[direction]:
			cur_item = item_assoc.get(self.urlname)
			flag = cur_item
			flag += ' ' 
			flag += self.urlname
			
			#take item into inventory, if its not already inside
			if not cur_item in inventory:
				inventory.append(cur_item)
				#mark that item taken 
				flag1 = FLAGS_ressource.get(flag)
				for x in FLAGS_flag_affectroom.get(flag1):
					flag_3 = " ".join([x, flag1])
					for x in FLAG_flag_affectdir.get(flag1):
						flag_compl = " ".join([x, flag_3])
						FLAGS_list.append(flag_compl)
					
					
		#same for events
		if direction in FLAGS_events and self.urlname in FLAGS_events[direction]:
			cur_event = event_assoc.get(self.urlname)
			flag = cur_event
			flag += ' ' 
			flag += self.urlname
			flag1 = FLAGS_ressource.get(flag)
			for x in FLAGS_flag_affectroom.get(flag1):
				flag_3 = " ".join([x, flag1])
				for x in FLAG_flag_affectdir.get(flag1):
					flag_compl = " ".join([x, flag_3])
					FLAGS_list.append(flag_compl)
		#check if there is an item requirement and if the item is in inventory
		if direction in item_req and item_req.get(direction, 'Error') in inventory:
			cur_item = item_req.get(direction)
			flag = event_assoc.get(self.urlname)
			flag += ' ' 
			flag += self.urlname
			
			#set flag for current item
			flag1 = FLAGS_ressource.get(flag)
			for x in FLAGS_flag_affectroom.get(flag1):
				flag_3 = " ".join([x, flag1])
				for x in FLAG_flag_affectdir.get(flag1):
					flag_compl = " ".join([x, flag_3])
					FLAGS_list.append(flag_compl)
				
			# remove item from inventory
			inventory.remove(cur_item)
		elif direction in item_req and not item_req.get(direction, 'Error') in inventory:
			direction +='_no_item'
		if '*' in self.paths.keys():
			default_direction = self.paths.get('*')
		return self.paths.get(direction, default_direction)
		
	def add_paths(self, paths):
		self.paths.update(paths) 

	
		
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

	
central_corridor = Scene("Central Corridor", "central_corridor", 
""" 
You head off into the direction where you reckon
the escape pod could be. You rush down a big gritty
corridor and suddenly walk into a fat and slightly smelly Gothon.
What are you going to do?
1. Try some small talk
2. Tell a short joke
3. Sucker punch that douche!
""")	
	
central_corridor_death1 = Scene("Central Corridor", "central_corridor_death1", 
""" 
After saying about five long sentences in a row
to introduce yourself, the Gothon looses it and slaps your head off
while grunting '20 Words or less!'
""")	
	
central_corridor_death2 = Scene("Central Corridor", "central_corridor_death2", 
""" 
Before you could move your fist even 2 inches towards him he
tears off your arm and stuffs it down your Throat.
You seem to be suprisingly dead after that.
""")	
	
central_corridor_live = Scene("Central Corridor", "central_corridor_alt", 
""" 
You tell the Gothon a joke. After a few awkward
seconds of silence he replies with a single
loud noise which you interprete as a laugh. After that he steps
aside, grunting 'You funny. Me likes you.'
Nodding approvingly, you move down the Corridor.
""")	

central_corridor_alt = Scene("Central Corridor", "central_corridor_alt", 
""" 
At the end of the corridor you see 3 doors.
Above each door you see a metal badge: 
1.'Laser Weapon Armory'
2.'Bridge'
3. Escapepods
Which one do you take?
""")	

laser_weapon_armory = Scene("Laser Weapon Armory", "laser_weapon_armory", 
""" You enter a room which seems to be some kind
Of armory. You find a neutron bomb which you could use
to blow up the ship right before escaping it,
but it's locked away inside an iron box.
The box has a keypad with the numbers 1,2 and 3
which you have to enter in a specific number.
Each number can only be entered once.
Enter it in format X-X-X
""")

laser_weapon_armory_box_open = Scene("Laser Weapon Armory", "laser_weapon_armory_box_open", 
""" 
You hear a 'click' and the metal box opens.
Carefully you pick up the small, white ball inside
and hide it in your pocket and leave the armory.
""")

laser_weapon_armory_box_wrong1 = Scene("Laser Weapon Armory", "laser_weapon_armory_box_wrong1", 
""" 
The metal box beeps in a intimidating way.
But it seems that you have 10 tries.
So you have 9 left.
""")

laser_weapon_armory_box_wrong2 = Scene("Laser Weapon Armory", "laser_weapon_armory_box_wrong2", 
""" 
The metal box beeps in an intimidating way.
Seems like it was the wrong number again. Try again.
""")

laser_weapon_armory_box_death = Scene("Laser Weapon Armory", "laser_weapon_armory_box_death", 
""" 
Seriously? It's only 3 numbers! You die of stupidity! "
""")

laser_weapon_armory_alt = Scene("Laser Weapon Armory", "laser_weapon_armory_alt" , 
"""
You already have the bomb. You should check out the other rooms.
""")

the_bridge = Scene("The Bridge", "the_bridge", 
""" You enter the middle door and notice that the room behind"
is the bridge of the ship. You notice too late that there"
is another Gothon in this room so you have to face him. "
What do you do?"
 1. Sing a lullaby"
 2. Tell him that he has beautiful eyes"
 3. Insult his mother"
""") 

#FLAG!
the_bridge_live = Scene("The Bridge", "the_bridge_live", 
""" 
You start singing a lullaby and soon after that you notice
that the Gothon looks very sleepy.
As soon as he starts snoring you pass him and go to the terminal.
""") 


the_bridge_death1 = Scene("The Bridge", "the_bridge_death1", 
"""
You tell the Gothon that his eyes look brigther
than all the stars in the universe. But for some reason
he doesn't seem very flustered. Instead
He vomits all over you. The caustic substance corrodes
your entire body into a smelly little puddle of gunk.
""") 


the_bridge_death2 = Scene("The Bridge", "the_bridge_death2", 
""" 
You tell the Gothon that his mother is so fat, that she is on
both sides of the family. After he has processed what you just
said, he grabs your head and pulls it off alongside your spine.
Just before you die you hear a deep voice murmuring 'FATALITY!'
""") 


the_bridge_alt = Scene("The Bridge", "the_bridge_alt", 
"""
 You stand infront of the beeping Terminal. 
""") 

the_bridge_no_bomb = Scene("The Bridge", "the_bridge_no_bomb", 
"""
 You dont have a bomb! Maybe look for one?
""") 

the_bridge_bomb = Scene("The Bridge", "the_bridge_bomb", 
"""
You take the Bomb out of your Pocket and place it on the Terminal.
You activate the Timer and run out of the room.
""")

escape_pod = Scene("Escape Pod", "escape_pod",
""" 
As you enter the right room, the first thing you see are the escape pods.
Unfortunately your happines about findingt it so easily is dulled a little by 
the fact that there are apparently three of them.
You remember vaguely that only one of them is actually working.
Which one do you take? 
""") 

the_end_winner = Scene("You Made It!", "the_end_winner", 
""" 
Whoohoo, you did it! You mate it our alive! But while you  are watching
your fireworks in the sky, you can't stop wondering who the hell that voice was 
which helped you figure out your plan...
""") 

the_end_loser = Scene("...", "the_end_loser",
 """
You try to start the pod, but the engine won't fire.
You explode alongside a pretty sound and light
provided by your own bomb.
Well, at least you killed the Gothons.
""") 

the_end_loser_nobomb = Scene("...", "the_end_loser_nobomb",
 """
'It worked' Thats what you thought right after arriving at the planet you escaped to.
And just before the Gothons blow you up alongside that entire planet.
Bad thing that planet had to be demolished for a galactic freeway.
""") 


generic_death = Scene("Death...", "death", "You died.")

#welcome screen transition to central corridor
welcome_screen.add_paths({
	'*': central_corridor
})


the_bridge.add_paths({
	'tell': generic_death,
	'insult': generic_death,
	'sing': the_bridge_live
})

laser_weapon_armory.add_paths({
	'3-1-2': laser_weapon_armory_box_open,
	'*': laser_weapon_armory_box_wrong2,
	'leave': central_corridor_alt
})

central_corridor_death1.add_paths({
	'*': generic_death
})

central_corridor_death2.add_paths({
	'*': generic_death
})
  

central_corridor_live.add_paths({
	'*': central_corridor_alt
})


central_corridor_alt.add_paths({
	'lwa':laser_weapon_armory,
	'bridge':the_bridge,
	'pods':escape_pod,
	'lwaalt':laser_weapon_armory_alt,
	'bridgealt':the_bridge_alt
})



laser_weapon_armory_box_open.add_paths({
	'*': central_corridor_alt
	})


laser_weapon_armory_box_wrong1.add_paths({
	'3-1-2': laser_weapon_armory_box_open,
	'leave': central_corridor_alt,
	'*': laser_weapon_armory_box_wrong2
})


laser_weapon_armory_box_wrong2.add_paths({
	'3-1-2': laser_weapon_armory_box_open,
	'leave': central_corridor_alt,
	'*': laser_weapon_armory_box_wrong2
})


laser_weapon_armory_box_death.add_paths({
	'*': generic_death
})

laser_weapon_armory_alt.add_paths({
	'*': central_corridor_alt
})

the_bridge_live.add_paths({
	'*': the_bridge_alt
})


the_bridge_death1.add_paths({
	'*': generic_death
})


the_bridge_death2.add_paths({
	'*': generic_death
})


the_bridge_alt.add_paths({
	'place bomb': the_bridge_bomb,
	'leave': central_corridor_alt,
	'place bomb_no_item': the_bridge_no_bomb
})


the_bridge_bomb.add_paths({
	'*': central_corridor_alt
})
the_bridge_no_bomb.add_paths({
	'*': central_corridor_alt
})


the_end_loser_nobomb.add_paths({
	'*': generic_death
})



escape_pod.add_paths({
	'1alt': the_end_loser,
	'2alt': the_end_winner,
	'3alt': the_end_loser,
	'*': the_end_loser_nobomb
})

central_corridor.add_paths({
    'talk':central_corridor_death1,
    'punch':central_corridor_death2,
    'joke': central_corridor_alt,
	})
	


SCENES = {
	welcome_screen.urlname: welcome_screen,
	central_corridor.urlname : central_corridor,
	laser_weapon_armory.urlname : laser_weapon_armory,
	the_bridge.urlname : the_bridge,
	escape_pod.urlname : escape_pod,
	the_end_winner.urlname : the_end_winner,
	the_end_loser.urlname : the_end_loser,
	generic_death.urlname : generic_death,
	central_corridor_death1.urlname : central_corridor_death1,
	central_corridor_death2.urlname : central_corridor_death2,
	central_corridor_live.urlname : central_corridor_live,
	central_corridor_alt.urlname : central_corridor_alt,
	laser_weapon_armory_box_open.urlname : laser_weapon_armory_box_open,
	laser_weapon_armory_box_wrong1.urlname : laser_weapon_armory_box_wrong1,
	laser_weapon_armory_box_wrong2.urlname : laser_weapon_armory_box_wrong2,
	laser_weapon_armory_box_death.urlname : laser_weapon_armory_box_death,
	laser_weapon_armory_alt.urlname : laser_weapon_armory_alt,
	the_bridge_live.urlname : the_bridge_live,
	the_bridge_death1.urlname : the_bridge_death1,
	the_bridge_death2.urlname : the_bridge_death2,
	the_bridge_alt.urlname : the_bridge_alt,
	the_bridge_bomb.urlname : the_bridge_bomb,
	the_bridge_no_bomb.urlname : the_bridge_no_bomb,
	the_end_loser_nobomb.urlname : the_end_loser_nobomb}


	
START = welcome_screen