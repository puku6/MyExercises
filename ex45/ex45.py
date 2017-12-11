from sys import exit 
from random import randint
import map2
prompt = "> "

global key_pickup
global couch_moved
global office_opened
global cellphone_pickup
global code_entered
global locket_pickup
global lid_pickup
global poison_pickup
global envelope_pickup
global video_pickup

class Room(object):

	
	def inperror(self, inp_room):	
		print "Input Error. Please Try again.\n"
		#print "debug: print inp_room %s" % inp_room
		return inp_room
		
	def add_inventory (self, inv_item, inp_room):
		global current_inventory
		current_inventory.append (inv_item)
		return inp_room
		
	def call_inventory (self, inp_room):
		print current_inventory
		
	def take_fingerprints (self, inp_room,inp_person ):
		if inp_person in current_inventory:
			print "You already have that print!"
		else:
			current_inventory.append ('Fingerprint %s' % inp_person)
			print "You took the fingerprints of the %s" % inp_person
	def take_fingerprints_item (self, input_unform, inp_room):
		input_form = input_unform.split(" ")
		cur_item = ' '.join(input_form[4:6])
		if (input_form[0]=='use' and input_form[1]=='Fingerprint' 
		and input_form[2]=='Set' and input_form[3]=='with'
		and ('Key' or 'Envelope' or 'Locket' 
		or 'Flash' or 'Cell' or 'Poison' or 'Lid'in cur_item )):
			cur_item = ' '.join(input_form[4:6])
			if cur_item not in current_inventory:
				print "You dont have this item (yet)!"
			elif cur_item == 'Poison':
				print "There are no prints on the glass of poison! Suspicious..."
			
			else:
				cur_print = 'Fingerprint %s' % cur_item
				if cur_print in current_inventory:
					print "You already have that print!"
				else: 
					current_inventory.append (cur_print)
					print "You took the fingerprints of the %s" % cur_item
		else: 
			
			self.inperror(inp_room)	
		
	
	def compare_fingerprints (self, inp_room, prints_unform):
		prints_form=prints_unform.split(" ")
		if (prints_form[0]=='use' and prints_form[1]=='Fingerprint' 
		and prints_form[3]=='with' and prints_form[4]=='Fingerprint'):
			print_1 =' '.join(prints_form[1:3])
			print_2 = ' '.join(prints_form[4:7])
			if (print_1 or print_2) not in current_inventory:
				print "You dont have this print yet!" 
			elif (((print_1 =='Fingerprint Lawyer' or print_2 == 'Fingerprint Lawyer')
			and (print_1 =='Fingerprint Flashdrive' or print_2=='Fingerprint Flashdrive')) 
			or ((print_1 =='Fingerprint Charlady' or print_2 == 'Fingerprint Charlady')
			and (print_1 == 'Fingerprint Locket' or print_2 == 'Fingerprint Locket')) 
			or ((print_1 == 'Fingerprint Victim' or print_2 == 'Fingerprint Victim')
			and (print_1 == 'Fingerprint Lid' or print_2 == 'Fingerprint Lid')) 
			or ((print_1 == 'Fingerprint Buisness Partner' or print_2 == 'Fingerprint Buisness Partner')
			and (print_1 == 'Fingerprint Key' or print_2 == 'Fingerprint Key')) 
			or ((print_1 == 'Fingerprint Victim' or print_2 == 'Fingerprint Victim')
			and (print_1 == 'Fingerprint Phone' or  print_2 == 'Fingerprint Phone'))
			or ((print_1 == 'Fingerprint Victim' or print_2 == 'Fingerprint Victim')
			and (print_1 == 'Fingerprint Lid' or  print_2 == 'Fingerprint Lid'))):
				print "They match!"
			elif ((print_1 == 'Fingerprint Lawyer' or print_2 == 'Fingerprint Lawyer')
			and (print_1 == 'Fingerprint Envelope' or print_2 == 'Fingerprint Envelope')):
				print "They match!... But there are more prints on the envelope!"
			elif ((print_1 == 'Fingerprint Charlady' or print_2 == 'Fingerprint Charlady')
			and (print_1 == 'Fingerprint Envelope' or print_2 == 'Fingerprint Envelope')) :
				print "They match!... But there are more prints on the envelope!"
			elif not (((print_1 =='Fingerprint Lawyer' or print_2 == 'Fingerprint Lawyer')
			and (print_1 =='Fingerprint Flashdrive' or print_2=='Fingerprint Flashdrive')) 
			or ((print_1 =='Fingerprint Charlady' or print_2 == 'Fingerprint Charlady')
			and (print_1 == 'Fingerprint Locket' or print_2 == 'Fingerprint Locket')) 
			or ((print_1 == 'Fingerprint Victim' or print_2 == 'Fingerprint Victim')
			and (print_1 == 'Fingerprint Lid' or print_2 == 'Fingerprint Lid')) 
			or ((print_1 == 'Fingerprint Buisness Partner' or print_2 == 'Fingerprint Buisness Partner')
			and (print_1 == 'Fingerprint Key' or print_2 == 'Fingerprint Key')) 
			or ((print_1 == 'Fingerprint Victim' or print_2 == 'Fingerprint Victim')
			and (print_1 == 'Fingerprint Phone' or  print_2 == 'Fingerprint Phone'))):
				print "They dont match."
			else:
				self.inperror(inp_room)
		else: 
			self.inperror(inp_room)	
			
	def help(self, inp_room):
		print "This is the help menu. "
		print "Commands: use x, enter x, talk to x, examine x, use x with y, leave, inventory, map, solve case"
		print "Other help topics: room, floor, fingerprint, show item to person "
		print "Type in one of commands or a help topic to get more help."
		print "All console input has to be typed in all lower case, if not specified otherwise."
		print "If you want to return to the game, type 'exit'."
		choice = raw_input(prompt)
		while choice != 'exit':
			print ""
			if 'use' in choice and not 'with' in choice:
				print "The 'use' command can be entered to use items from you inventory (like your flashlight). "
				print "Just type it in like 'use flashlight'."
			elif 'enter' in choice: 
				print "The 'enter' command is used to navigate around the house. "
				print "If u want to enter a room, type it in like 'enter diningroom'."
				print " All rooms have to be written in one word, the only exception "
				print "being the two livingroomss: They have to be typed in like this: "
				print "'enter livingroom 1' or 'enter livingroom 2'."
			elif 'talk to' in choice: 
				print "The 'talk to' command is used to communicate with other people inside the house."
				print "Type it in like:"
				print "'talk to son'."
			elif 'examine' in choice: 
				print "The 'examine' command is used to investigate the area around you. "
				print "If u find an item while examining, it will automaticly placed into your inventory. "
				print "Example: 'examine table'"
			elif 'use' and 'with' in choice: 
				print "The 'use with' command can be entered in three ways: "
				print "The first way is to use an item in your inventory to "
				print "interact with an item in your enviroment. "
				print "Example: 'use key with chest'. "
				print "The second way is to show people an item from your inventory. "
				print "Example: 'use flower with wife'. "
				print "The last way is to use two items from your inventory with each other. "
				print "Example: 'use fish with fishglass'. "
				print "For usage of the fingerprints, type in 'fingerprints'. "
			elif 'leave' in choice: 
				print "If you want to leave a room and return to the corridor, just type in 'leave'."
			elif 'inventory' in choice: 
				print "If you want to see your current inventory, just type in 'inventory'."
			elif 'map' in choice: 
				print "The command 'map' shows you a map of the house. The x marks your current position."
				print "The '/' symbol marks doors you can pass."
			elif 'room' in choice: 
				print "All rooms have to be written in one word and all lowercase, the only exception "
				print "being the two livingroomss: They have to be typed in like this: "
				print "'enter livingroom 1' or 'enter livingroom 2'."
			elif 'floor' in choice: 
				print "To use the stairs, you have to be in one of the games corridors. "
				print "The floors are: 'basement', 'first floor' and 'ground floor'."
				print "Then you type in your desired floor in the following format:"
				print "'enter basement'"
			elif 'fingerprint' in choice: 
				print "If you want to take fingerprints, you can use the fingerprint set in your inventory. "
				print "You can use it through the command 'use Fingerprint Set with x'. "
				print "You can use it with persons or items in your inventory."
				print "After you have taken the fingerprints, you can compare them with each other."
				print "But careful: The fingerprints, the fingerprint set and the items have to be written in uppercase!!"
				print "These are the only commands where you have to write in uppercase!"
				print "Example: 'use Fingerprint Set with Knife' and 'use Fingerprint Knife with Fingerprint Murderer'"
			elif 'show' in choice:
				print "To show an item to someone, use the 'use x with y' command."
			elif 'help' in choice:
				print "This is the help menu. "
				print "Commands: use x, enter x, talk to x, examine x, use x with y, leave, inventory, map"
				print "Other help topics: room, floor, fingerprint, show item to person "
				print "Type in one of commands or a help topic to get more help."
				print "All console input has to be typed in all lower case, if not specified otherwise."
				print "If you want to return to the game, type 'exit'."
			elif 'solve' in choice:
				print "To solve the case, go into the entrance corridor on the ground floor and type in 'solve case'."
			else:
				print "Thats not a choice, silly."
			choice = raw_input(prompt)
		return inp_room
		
	def getmap(self, inp_room):	
		print maplist[inp_room]
		print ""
class Engine(object):
		
		def __init__(self, room_map):
			self.room_map = room_map 
			
		def play(self):
			room_name = self.room_map.start_room
			
			#print "current scene name %s" %room_name
			#print "start loop"	
			
			while room_name != 'end_screen':				 
				#print "starting scene name is %s " % room_name
				current_room=self.room_map.next_room(room_name)	
				
				#print "got scene_name %s" % current_room
				room_name = current_room.enter()
				#print "room name is %s" % room_name
				#print "restart scene loop"
				
			
			
class WelcomeScreen():
	def enter(self):
		global current_inventory
		global key_pickup
		global video_pickup
		global office_opened
		global cellphone_pickup
		global code_entered
		global locket_pickup
		global lid_pickup
		global poison_pickup
		global flashlight_on
		global envelope_pickup

		envelope_pickup = False
		flashlight_on = False
		poison_pickup = False
		lid_pickup = False
		code_entered = False
		office_opened = False
		video_pickup = False
		key_pickup = False
		cellphone_pickup = False 
		locket_pickup = False
		current_inventory = ['Flashlight', 'Fingerprint Set']
		print "Welcome to the mysterious morder at the cottage! A rich bankier has been found dead "
		print "this morning in his cottage. His charlady found him dead inside the "
		print "cabinet for cleaning supplies and you, the detective, have been called to solve this case. "
		print "It is monday afternoon and you made sure that all suspects jhave been called to the cottage as well."
		print "The suspects are the victims wife, their son, the charlady who found the body,"
		print "the family lawyer and the bankiers buisness partner. Who killed him, where,"
		print "when and what was the murder weapon?"
		print "Do you now want to enter the house? Enter Yes or No."
		choice = raw_input(prompt)
		if choice == 'Yes':
			print "You enter the house."
			return 'entrance_corridor'
		elif choice == 'No':
			print "You decide that you won't solve this case. You never liked bankers anyways, "
			print "so one member less of this species doesnt bother you. You leave."
			quit()
		else:
			print "Please enter Yes or No to continue."
			return 'welcome_screen'

class SolveScreen(Room):
	def enter(self):
		print "Please enter the name of the murderer, the murder weapon and the crime scene."
		choice = raw_input(prompt)
		if ('lawyer' and ('bottle' or 'water') and ('poison' or 'poisoned') 
		and 'sauna') in choice:
			print "Congratulations! You solved the case!"
			print "The lawyer is the murderer. He has an affair with the bankers wife "
			print "and he also drew up their prenuptial agreement. "
			print "He knows that there is no way out of this contract and if the banker "
			print "and his wife get divorced, the wife won't get anything. "
			print "\nThe wife liked her husband especially in combination with his money. "
			print "Even though she didnt love him as much as at the beginning of ther relationship, "
			print "she still felt a strong bond between them and would never have killed him."
			print "\nThe son couldn't have done it because his pacifist ideals "
			print "would stop him from commiting murder."
			print "\nThe charlady also wouldn't have killed him,"
			print " even though she stole the money from the safe, because she loved the victim."
			print "\nThe buisness partner is also not the murderer, because he has a solid alibi. "
			print "He broke into the bankers office and got caught on camera while the murder happened. "
			print "\nThe lawyer knew that the banker was suspecting his wife to have an affair because he told him about it. "
			print "He panicked because he knews that in case of a divorce, the wife would get nothing and "
			print "that she would never choose to stay with him under these circumstances. "
			print "So he killed the banker, knowing that the wife would be the only heir and "
			print "hoping that she would get with him after her husband died."
		else:
			print "Sorry, that doesn't seem to be what happened."
			print "Maybe you should investigate some more."
			return 'entrance_corridor'
			# Rooms EG	
class EntranceCorridor(Room):

	def enter(self):
		inp_room = 'entrance_corridor'
		global office_opened
		global current_inventory
		print "You are standing in a big hallway with several doors. There are also two stairways, "
		print "one leading up into the first floor and the other one down into the basement. "
		print "The doors seem to lead into a livingroom, a WC, an office, "
		print "a diningroom with an attached kitchen and a second livingroom. "
		print "Where do you want to go?"
		choice = raw_input(prompt)
		if choice == 'enter livingroom 1':
			return 'livingrm1_eg'
		elif choice == 'enter diningroom':
			return 'diningrm_eg'
		elif choice == 'enter wc':
			return 'wc_eg'
		elif choice == 'enter office' and office_opened == False and 'Key' in current_inventory:
			print "It worked! The key opened the door. "
			office_opened = True
			return 'office_eg'
		elif choice == 'enter office' and office_opened == False:
			print "You try to open the door to the office, but it seems that it is locked."
			return inp_room
		elif choice == 'enter office' and office_opened == True:
			return 'office_eg'
		elif choice == 'enter livingroom 2':
			return 'livingrm2_eg'
		elif choice == 'enter basement':
			print "You take the stairs down into the basement."
			return 'corridor_bs'
		elif choice == 'enter first floor':
			print "You decide to go upstairs."
			return 'entrance_corridor2'
		elif choice == 'inventory':
			self.call_inventory(inp_room)
			return inp_room
		elif choice == 'debug prints':
			current_inventory.append('Fingerprint Lawyer')
			current_inventory.append('Fingerprint Flashdrive')
			current_inventory.append('Fingerprint Envelope')
			print "Debug successful."
			return inp_room
		elif ('use' and 'Fingerprint' and 'with') in choice and not ('Set' in choice):
			self.compare_fingerprints (inp_room, choice)
			return inp_room
		elif 'help' in choice:
			self.help(inp_room)
			return inp_room
		elif choice == 'map':
			map2.getmap_module(inp_room)
			return inp_room
		elif ('use' and 'fingerprint set' and 'with') in choice: 
			self.take_fingerprints_item(choice, inp_room)
			return inp_room
		elif 'use' in choice:
			print "This isnt the time to use that!"
			return inp_room
		elif choice == 'solve case':
			return 'solve_screen'
		else:
			error = self.inperror(inp_room)
			return error 
class ToiletEG(Room):

	def enter(self):
		inp_room = 'wc_eg'
		print "You enter the WC next to the entrance. "
		print "It looks like a normal WC. You see a toilet and a basin."
		print "What do you want to do?"
		choice = raw_input(prompt)
		if choice == 'examine toilet':
			print "You examine the toilet."
			print "It looks pretty normal and is probably"
			print "not related to the case."
			return inp_room
		elif choice == 'examine basin':
			print "You take a closer look at the basin."
			print "It is pretty big and the tap is golden with "
			print "lot of fancy features. It must have been expensive."
			return inp_room
		elif choice == 'leave':
			return 'entrance_corridor'	
			
		elif ('use' and 'Fingerprint' and 'with') in choice and not ('Set' in choice):
			self.compare_fingerprints (inp_room, choice)
			return inp_room

		elif choice == 'inventory':
			self.call_inventory(inp_room)
			return inp_room			
			
		elif ('help' or 'Help') in choice:
			self.help(inp_room)
			return inp_room
		
		elif choice == 'map':
			map2.getmap_module(inp_room)
			return inp_room	
		elif ('use' and 'fingerprint set' and 'with') in choice: 
			self.take_fingerprints_item(choice)
			return inp_room
		else:
			error = self.inperror(inp_room)
			return error 
		
class Livingroom1EG(Room):

	def enter(self):
		inp_room = 'livingrm1_eg'
		global key_pickup
		print "You enter the livingrooms near the entrance."
		print "You can see a picture hanging from the wall,"
		print "a couch, a big chandelier and the son of the victim"
		print "standing next to the window."
		print "What will you do?"
		choice = raw_input(prompt)
		if choice == 'examine couch' and key_pickup == False:
			print "You take a closer look at the couch."
			print "It looks pretty comfortable."
			print "It is a great place to relax."
			print "As you look in the cracks in the couch you can see something shiny."
			print "You put in your hand to grab the item and pull out a key."
			print "Did somebody hide it there? "
			print "The key has been added to your inventory.\n"
			key_pickup = True 
			item_room = self.add_inventory('Key', inp_room)
			return item_room
		elif choice == 'examine couch':
			print "You take a closer look at the couch."
			print "It looks pretty comfortable."
			print "It is a great place to relax."
			print " "
			return inp_room
		elif choice == 'pick debug':
			self.add_inventory('Debug')
		elif choice == 'talk to son':
			print "You talk to the 25 year old son and notice that "
			print "he doesn't seem too sad about his fathers premature demise."
			print "You ask him why and he admits that he doesn't have "
			print "the best relationship with his parents. "
			print "He complains about them being selfisch and never thinking about others."
			print "He then goes on to lecture you about communist values and that"
			print "everybodies life is equally precious and should not be wasted, "
			print "no matter if the person is a homeless or a millionair.\n"
			return inp_room
		elif (choice == 'use Fingerprint Set with Son' or 
		choice == 'use fingerprint set with son'):
			self.take_fingerprints(inp_room, 'Son')
			return inp_room
		elif choice == 'examine chandelier':
			print "You take a closer look at the chandelier. "
			print "It is very pretty und must have been really expensive. \n"
			return inp_room
		elif choice == 'examine picture': 
			print "You take a closer look at the picture."
			print "It shows a mountain landscape."
			print "It's probably not related to the case."
			return inp_room
		elif choice == 'leave':
			return 'entrance_corridor'
			
		elif choice == 'inventory':
			self.call_inventory(inp_room)
			return inp_room			
			
		elif ('help' or 'Help') in choice:
			self.help(inp_room)
			return inp_room
		
		elif choice == 'map':
			map2.getmap_module(inp_room)
			return inp_room	
			
		elif ('use' and 'Fingerprint' and 'with') in choice and not ('Set' in choice):
			self.compare_fingerprints (inp_room, choice)
			return inp_room
		elif ('use' and 'fingerprint set' and 'with') in choice: 
			self.take_fingerprints_item(choice, inp_room)
			return inp_room
			
		elif 'use' in choice:
			print "This isnt the time to use that!"
			return inp_room
		else:
			error = self.inperror('livingrm1_eg')
			return error
		
class DiningroomEG(Room):

	def enter(self):
		inp_room = 'diningrm_eg'
		global video_pickup
		print "As you step inside the diningroom you see a large table"
		print "with many chairs, a hutch in the corner and a door leading into the kitchen. "
		print "What do you want to do?"
		choice = raw_input(prompt)
		if choice == 'examine chairs':
			print "You examine the chairs."
			print "They are made of cherry wood and look comfortable."
			return 'diningrm_eg'
		elif choice == 'examine table':
			print "You look closely at the table. It is very big and doesn't seem related to the case."
			return 'diningrm_eg'
		elif choice == 'enter kitchen':
			return 'kitchen_eg'
		elif choice == 'examine hutch' and video_pickup == False:
			print "You open the hutch and see a lot of expensive looking"
			print "plates and glasses inside."
			print "Oh, it seems like someone has hidden a little flashdrive between"
			print "the plates."
			print "The flashdrive has been added to you inventory."
			video_pickup = True
			item_room = self.add_inventory('Flashdrive', inp_room)
			return inp_room
		elif choice == 'examine hutch' and video_pickup == True:
			print "You open the hutch and see a lot of expensive looking"
			print "plates and glasses inside."
			return inp_room
		elif choice == 'leave':
			return 'entrance_corridor'
			
		elif choice == 'inventory':
			self.call_inventory(inp_room)
			return inp_room			
			
		elif ('help' or 'Help') in choice:
			self.help(inp_room)
			return inp_room
		
		elif choice == 'map':
			map2.getmap_module(inp_room)
			return inp_room	
			
		elif ('use' and 'Fingerprint' and 'with') in choice and not ('Set' in choice):
			self.compare_fingerprints (inp_room, choice)
			return inp_room
		elif ('use' and 'fingerprint set' and 'with') in choice: 
			self.take_fingerprints_item(choice, inp_room)
			return inp_room
			
		elif 'use' in choice:
			print "This isnt the time to use that!"
			return inp_room
		else:
			error = self.inperror(inp_room)
			return error
class KitchenEG(Room):

	def enter(self):
		inp_room = 'kitchen_eg'
		print "You enter the kitchen. There are a stove, a fridge and a sink."
		print "Everything looks pretty neat and clean. "
		print "What do you want to do?"
		choice = raw_input(prompt)
		if choice == "examine sink":
			print "You examine the sink. It looks pretty average but clean"
			return inp_room
		elif choice == "examine stove":
			print "You look inside the oven underneath the stove. "
			print "There is nothing inside besides the smell of baked food."
			return inp_room
		elif choice == "examine fridge":
			print "You look inside the fridge. There is a lot of food inside. "
			print "It was filled because the victim spend the weekend in this house,"
			print "when he was visited by a murderer."
			return inp_room
		elif choice == 'leave':
			return 'diningrm_eg'
			
		elif choice == 'inventory':
			self.call_inventory(inp_room)
			return inp_room			
			
		elif ('help' or 'Help') in choice:
			self.help(inp_room)
			return inp_room
		
		elif choice == 'map':
			map2.getmap_module(inp_room)
			return inp_room	
			
		elif ('use' and 'Fingerprint' and 'with') in choice and not ('Set' in choice):
			self.compare_fingerprints (inp_room, choice)
			return inp_room
		elif ('use' and 'fingerprint set' and 'with') in choice: 
			self.take_fingerprints_item(choice, inp_room)
			return inp_room
			
		elif 'use' in choice:
			print "This isnt the time to use that!"
			return inp_room
		else:
			error = self.inperror(inp_room)
			return error 
	
class Livingroom2EG(Room):

	def enter(self):
		inp_room = 'livingrm2_eg'
		print "You enter the second livingrooms. "
		print "Inside you meet the victims buisness partner. "
		print "Other than him you see a painting, a couch and an armchair. "
		print "What do you want to do?"
		choice = raw_input(prompt)
		if choice == 'examine painting':
			print "You take a closer look at the painting. It shows a sailing ship."
			print "On the sail you can see the number 4062."
			return inp_room
		elif choice == 'examine couch':
			print "The couch looks very comfy. "
			print "But you don't have the time to sit down and relax!"
			print "You need to catch a murderer!"
			return inp_room
		elif choice == 'talk to buisness partner':
			print "You ask the buisness partner where he has been saturday night "
			print "and if he was angry about for you have heard that he betrayed him,"
			print " causing him to loose several million punds. "
			print "The buisness partner states that he was alone "
			print "by himself on saturday night. He then goes on to "
			print "admit that he was very angry, but he swears that he didn't kill him."
			return inp_room
		elif (choice == 'use fingerprint set with buisness partner' or
		choice == 'use Fingerprint Set with Buisness Partner'):
			self.take_fingerprints(inp_room, 'Buisness Partner')
			return inp_room
			
		elif choice == 'leave':
			return 'entrance_corridor'
			
		elif choice == 'inventory':
			self.call_inventory(inp_room)
			return inp_room			
			
		elif ('help' or 'Help') in choice:
			self.help(inp_room)
			return inp_room
		
		elif choice == 'map':
			map2.getmap_module(inp_room)
			return inp_room	
			
		elif ('use' and 'Fingerprint' and 'with') in choice and not ('Set' in choice):
			self.compare_fingerprints (inp_room, choice)
			return inp_room
		elif ('use' and 'fingerprint set' and 'with') in choice: 
			self.take_fingerprints_item(choice, inp_room)
			return inp_room
			
		elif 'use' in choice:
			print "This isnt the time to use that!"
			return inp_room
		else: 
			error = self.inperror(inp_room)
			return error
class OfficeEG(Room):

	def enter(self):
		inp_room = 'office_eg'
		global envelope_pickup
		global current_inventory
		print "Inside the the office you see a book case, a work desk and "
		print "on top of it a laptop. What do you want to do?"
		choice = raw_input(prompt)
		if choice == 'examine book case':
			print "As you look through the folders in the bookcase you find one which "
			print "contains important documents. You investigate it closely "
			print "and find a prenuptial agreement signed by the victim and his wife, "
			print "saying that in case of a divortion, the wife would get almost nothing. "
			print "You also find out that the lawyer was the one to draw up this contract. "
			print "Right behind the contract you find prepared divorce papers drawn up"
			print "by the lawyer about a week ago and a letter from the lawyer to the victim. "
			print "It says that the lawyer doesn't believe that the bankier is right "
			print "about his wife cheating on him and that he must not act with precipitation. "
			print "It also says that he prepared the divorce paper anyway just like he was asked to. "
			return inp_room
		elif choice == 'examine work desk' and envelope_pickup == False:
			print "On the work desk you find an envelope adressed to the victim. "
			print "It looks like it has been already opened. It's empty now. "
			print "According to the details on the envelope the sender must have been "
			print "the bankiers secretary. "
			print "The postal stamp tells you that it must have arrived this morning. "
			print "The envelope has been added to your inventory."
			envelope_pickup = True
			item_room = self.add_inventory('Envelope', inp_room)
			return inp_room
		elif choice == 'examine work desk' and envelope_pickup == True:
			print "The work desk is empty now."
			return inp_room
		elif choice == 'examine laptop':
			print "You examine the laptop. It doesn't contain any documents "
			print "connected to the case, but it has an USB-Port."
			return inp_room
		elif choice == 'use flashdrive with laptop' and 'Flashdrive' in current_inventory:
			print "You use the laptop to see what is on the flashdrive. "
			print "It contains a video which has been recorded by a survaillance camera."
			print " It shows the buisness partner of the victim breaking in into what "
			print "seems to be a bank office. It must be the victims working place. "
			print "The time stamp shows that this video was recorded on saturday night; "
			print "That was exactly when the victim was killed."
			return inp_room
		elif choice == 'leave':
			return 'entrance_corridor'
			
		elif choice == 'inventory':
			self.call_inventory(inp_room)
			return inp_room			
			
		elif ('help' or 'Help') in choice:
			self.help(inp_room)
			return inp_room
		
		elif choice == 'map':
			map2.getmap_module(inp_room)
			return inp_room	
			
		elif ('use' and 'Fingerprint' and 'with') in choice and not ('Set' in choice):
			self.compare_fingerprints (inp_room, choice)
			return inp_room
		elif ('use' and 'fingerprint set' and 'with') in choice: 
			self.take_fingerprints_item(choice, inp_room)
			return inp_room
			
		elif 'use' in choice:
			print "This isnt the time to use that!"
			return inp_room
		else:
			error = self.inperror(inp_room)
			return error 

# Rooms Basement		
class CorridorBasement(Room):

	def enter(self):
		inp_room = 'corridor_bs'
		print "In the basement corridor you can see three doors leading into a laundryroom,"
		print "a sauna and a storageroom. Where do you want to go?"
		choice = raw_input(prompt)
		if choice == "enter laundryroom":
			return 'laundry_bs'
		elif choice == 'enter sauna':
			return 'sauna_bs'
		elif choice == 'enter storageroom':
			return 'storage1_bs'
		elif choice == 'enter ground floor':
			print "You take the stairs back into the ground floor."
			return 'entrance_corridor'
		else:
			error = self.inperror(inp_room)
			return error
			
class LaundryBasement(Room):

	def enter(self):
		inp_room = 'laundry_bs'
		print "You enter the laundryroom, where you meet the upset charlady."
		print "She is kneeling next to the dead body and can't help but cry."
		print " Other then her and the body, there is a washing machine and the"
		print "cabinet in which the body has been found."
		print "What do you want to do?"
		choice = raw_input(prompt)
		if choice == 'examine body':
			print "You examine the body and notice that the victim has no external injuries."
			print "You determine that the victim must have died on saturday night "
			print "between 9 and 12 pm. As you look at his feet, you realise, "
			print "that his left sock is the wrong way up."
			print "That is pretty strange for a tidy and neat man like him."
			return inp_room
		elif choice == 'examine washing machine':
			print "You look at the washing machine. You can't find anything special about it."
			print "It might not be relevant to the case."
			return inp_room
		elif choice == 'examine cabinet':
			print "You investigate the cabinet where the body was found. "
			print "But apart from a lot of cleaning supplies and an unpleasant smell of death "
			print "you can't find anything."
			return inp_room
		elif choice == 'talk to charlady':
			print "You ask the charlady how and when exactly she found the body. "
			print "She tells you that she found it this morning around 9am when "
			print "she came to clean the house. She emptied the letter box, "
			print "sorted everything that was lying around and went to the laundryroom "
			print "to get her cleaning supplies. As she opened the cabinet, "
			print "the dead body just fell out of it. It took her about 10 minutes "
			print "to recover from the shock. After that, she immediatly called the police. "
			print "She tells you that the victim was a very good man and you seeher eyes watering up again."
			return inp_room
		elif choice == 'use locket with charlady' and 'Locket' in current_inventory:
			print "As you show the charlady the locket, she can't hold back anymore "
			print "and starts crying out loud. She admits that she has been secretly "
			print "in love with the victim which is why she has a locket like this. "
			print "As you tell her where you found it she gets very nervous. "
			print "She finally confesses that she stole money from the safe room after "
			print "she found the body because she really needed it. She only gets payed "
			print "very little for her job which she even might loose now and that "
			print "mercenary wife of his will still have more than enough to live."
			print "It seems that the victim was the only reason for her "
			print "to keep doing this low wage and unpleasant job."
			return inp_room
		elif choice == 'use envelope with charlady' and 'Envelope' in current_inventory:
			print "You show the opened envelope you've found on the victims working desk "
			print "to the charlady. She tells you that she found it in the letterbox "
			print "this morning and put it on the workdesk. "
			print "As she placed it there it was apparently still sealed."
			return inp_room
		elif (choice == 'use fingerprint set with charlady' 
		or choice == 'use Fingerprint Set with Charlady'):
			self.take_fingerprints(inp_room, 'Charlady')
			return inp_room
		elif (choice == 'use fingerprint set with body' 
		or choice == 'use Fingerprint Set with Body'):
			self.take_fingerprints(inp_room, 'Victim')
			return inp_room
			
		elif choice == 'leave':
			return 'corridor_bs'
			
		elif choice == 'inventory':
			self.call_inventory(inp_room)
			return inp_room			
			
		elif ('help' or 'Help') in choice:
			self.help(inp_room)
			return inp_room
		
		elif choice == 'map':
			map2.getmap_module(inp_room)
			return inp_room	
			
		elif ('use' and 'Fingerprint' and 'with') in choice and not ('Set' in choice):
			self.compare_fingerprints (inp_room, choice)
			return inp_room
		elif ('use' and 'fingerprint set' and 'with') in choice: 
			self.take_fingerprints_item(choice, inp_room)
			return inp_room
			
		elif 'use' in choice:
			print "This isnt the time to use that!"
			return inp_room
		else:
			error = self.inperror(inp_room)
			return error
			
class SaunaBasement(Room):

	def enter(self):
		inp_room = 'sauna_bs'
		global lid_pickup
		print "You enter the sauna. It is pretty small and there are "
		print "a bench and a sauna stove inside. You can still smell " 
		print "the last sauna infusion. It must have contained eukalyptus."
		choice = raw_input(prompt)
		if choice == 'examine sauna stove':
			print "You examine the sauna stove but you "
			print "can't find anything suspicious about it. "
			print "It smells strongly of eukalyptus, "
			print "indicating that it must have been used recently."
			return inp_room
		elif choice == 'examine bench' and lid_pickup == False:
			print "You take a close look at the bench. "
			print "Underneath it you find the lid of a water bottle. "
			print "The lid has been added to your inventory."
			lid_pickup = True
			item_room = self.add_inventory('Lid', inp_room)
			return item_room
		elif choice == 'examine bench' and lid_pickup == False:
			print "You take a close look at the bench. "
			print "There is nothing underneath it."
			return inp_room
		elif choice == 'leave':
			return 'corridor_bs'
			
		elif choice == 'inventory':
			self.call_inventory(inp_room)
			return inp_room			
			
		elif ('help' or 'Help') in choice:
			self.help(inp_room)
			return inp_room
		
		elif choice == 'map':
			map2.getmap_module(inp_room)
			return inp_room	
			
		elif ('use' and 'Fingerprint' and 'with') in choice and not ('Set' in choice):
			self.compare_fingerprints (inp_room, choice)
			return inp_room
		elif ('use' and 'fingerprint set' and 'with') in choice: 
			self.take_fingerprints_item(choice, inp_room)
			return inp_room
			
		elif 'use' in choice:
			print "This isnt the time to use that!"
			return inp_room
		else: 
			error = self.inperror (inp_room)
			return error
			
class Storage1Basement(Room):

	def enter(self):
		inp_room = 'storage1_bs'
		global poison_pickup
		global flashlight_on
		if flashlight_on == False:
			print "You enter the storageroom and "
			print "notice that the light is broken. You can't see anything."
			print "What do you do?"
			choice = raw_input()
			if choice == 'use flashlight':
				print "You switch on your flashlight and..."
				flashlight_on = True
				return inp_room
			elif choice == 'leave':
				return 'corridor_bs'
			
			elif choice == 'inventory':
				self.call_inventory(inp_room)
				return inp_room			
				
			elif ('help' or 'Help') in choice:
				self.help(inp_room)
				return inp_room
			
			elif choice == 'map':
				map2.getmap_module(inp_room)
				return inp_room	
				
			elif ('use' and 'Fingerprint' and 'with') in choice and not ('Set' in choice):
				self.compare_fingerprints (inp_room, choice)
				return inp_room
			elif ('use' and 'fingerprint set' and 'with') in choice: 
				self.take_fingerprints_item(choice, inp_room)
				return inp_room
				
			elif 'use' in choice:
				print "This isnt the time to use that!"
				return inp_room
			else:
				error = self.inperror(inp_room)
				return error
		elif flashlight_on == True:			
			print "You can now see shelves on three of the walls."
			choice = raw_input(prompt)
			if choice == 'examine shelves' and poison_pickup == False:
				print "The shelves contain all kinds of canned food, bottles of water and many "
				print "other alcohic and non alcoholic drinks. Behind a can of beans "
				print "you find a small bottle of what seems to be poison. Could that have been the murder weapon?"
				print "The bottle of poison has been added to your inventory."
				poison_pickup = True
				item_room = self.add_inventory('Poison', inp_room)
				return item_room
			elif choice == 'examine shelves':
				print "The shelves contain all kinds of canned food, bottles of water and many "
				print "other alcohic and non alcoholic drinks. "
				return inp_room
			elif 'use lid' in choice and 'Lid' in current_inventory:
				print "You compare the lid you've found to the water bottles in this room."
				print "They match."
				return inp_room
			elif choice == 'leave':
				print "You turn off your flashlight and leave."
				flashlight_on = False
				return 'corridor_bs'
				
			elif choice == 'inventory':
				self.call_inventory(inp_room)
				return inp_room			
				
			elif ('help' or 'Help') in choice:
				self.help(inp_room)
				return inp_room
			
			elif choice == 'map':
				map2.getmap_module(inp_room)
				return inp_room	
				
			elif ('use' and 'Fingerprint' and 'with') in choice and not ('Set' in choice):
				self.compare_fingerprints (inp_room, choice)
				return inp_room
			elif ('use' and 'fingerprint set' and 'with') in choice: 
				self.take_fingerprints_item(choice, inp_room)
				return inp_room
				
			elif 'use' in choice:
				print "This isnt the time to use that!"
				return inp_room
				
			else:
				error = self.inperror(inp_room)
				return error
		else:
			error = self.inperror(inp_room)
			return error
				
# Rooms First Floor		
class EntranceCorridor2(Room):
	def enter(self):
		inp_room = 'entrance_corridor2'
		print "There are five rooms in this floor: A bathroom, a WC, "
		print "a guestroom, a bedroom and a kids bedroom. Where do you want to go?"
		choice = raw_input(prompt)
		if choice == 'enter guestroom':
			return 'guestroom1_f1'
		if choice == 'enter bedroom':
			return 'bedroom_f1'
		if choice == 'enter kids bedroom':
			return 'bedroomkids1_f1'
		elif choice == 'enter bathroom':
			return 'bathroom_f1'
		elif choice == 'enter wc':
			return 'wc_f1'
		elif choice == 'enter ground floor':
			print 'You take the stairs down back into the ground floor.'
			return 'entrance_corridor'
		else: 
			error = self.inperror(inp_room)
			return error
class Guestroom1FirstFloor(Room):
	def enter(self):
		inp_room = 'guestroom1_f1'
		print "You enter the guestroom in which you find the lawyer pacing up and down."
		print "Apart from that you see a bed, a suitcase and a closet."
		print "What do you want to do?"
		choice = raw_input(prompt)
		if choice == 'examine bed':
			print "The bed looks freshly made. "
			print "You can't find anything particullary interesting."
			return inp_room
		elif choice == 'examine closet':
			print "You examine the closet and open it, but it's completly empty."
			return inp_room
		elif choice == 'examine suitcase':
			print "As you make a move to open the suitcase, the lawyer stops you, "
			print "telling you that it is his. You ask him, why he brought it and he answers, "
			print "that as a close friend of the family he wants to stay "
			print "and help the widow with everything."
			return inp_room
		elif choice == 'talk to lawyer':
			print "You talk to the lawyer and ask him about his relationship with the victim. "
			print "After moaning about how tragic the victims death is, "
			print "he explains that he has been his privat lawyer for over 20 years now, "
			print "managing everything he was needed for. "
			print "He sighs and states that he will now do everything to fulfill his last wish "
			print "and help out so that everything will go smoothly with his will."
			return inp_room
			
		elif (choice == 'use fingerprint set with lawyer' 
		or choice == 'use Fingerprint Set with Lawyer') :
			self.take_fingerprints(inp_room, 'Lawyer')
			return inp_room
		elif choice == 'leave':
			return 'entrance_corridor2'
			
		elif choice == 'inventory':
			self.call_inventory(inp_room)
			return inp_room			
			
		elif ('help' or 'Help') in choice:
			self.help(inp_room)
			return inp_room
		
		elif choice == 'map':
			map2.getmap_module(inp_room)
			return inp_room	
			
		elif ('use' and 'Fingerprint' and 'with') in choice and not ('Set' in choice):
			self.compare_fingerprints (inp_room, choice)
			return inp_room
		elif ('use' and 'fingerprint set' and 'with') in choice: 
			self.take_fingerprints_item(choice, inp_room)
			return inp_room
			
		elif 'use' in choice:
			print "This isnt the time to use that!"
			return inp_room
		else:
			error = self.inperror(inp_room)
			return error
class BedroomFirstFloor(Room):

	def enter(self):
		inp_room = 'bedroom_f1'
		global cellphone_pickup
		print "You enter the bedroom and see the victims widow sitting on the bed crying. "
		print "There is also a closet, a nightstand and a door leading into a small bathroom."
		print "What do you want to do?"
		choice = raw_input(prompt)
		if choice == 'examine bed':
			print "The bed is king sized and has two blankets and big pillows. "
			print "A few smaller extra pillows add a special touch of cosyness."
			return inp_room
		elif choice == 'examine closet':
			print "You examine the closet and find a bunch of different clothes inside, "
			print "of which some must have belonged to the victim while others "
			print "seem to be the ones of his wife."
			return inp_room
		elif choice == 'examine nightstand' and cellphone_pickup == False:
			print "You look inside the nightstand. Inside you find a cell phone. "
			print "As you ask the wife about it, she tells you that it belonged to her husband. "
			print "She also seems surprised that you found it in there and tells you "
			print "that he normally takes it with him wherever he goes, "
			print "except for the bathroom and sauna. "
			print "She had expected you to find the cellphone in one of the victims pockets. "
			print "The cellphone has been added to you inventory."
			item_room = self.add_inventory('Phone', inp_room)
			cellphone_pickup = True 
			return inp_room
		elif choice == 'examine nightstand':
			print "You look inside the nightstand again. "
			print "There seems to be nothing else relevant to the case."
			return inp_room
		elif choice == 'talk to wife':
			print "As you try to talk to the wife she has trouble to stop "
			print "the tears from running down her cheeks. "
			print "You notice, that he expression shows not only sadness, but also guilt."
			print " You look straight into her eyes and ask her, what she feels so guilty about. "
			print "She looks shocked and quickly looks down while her face starts turning red. "
			print "She confesses, that she had an affaire and that she now feels bad about it."
			print " She admits that throughout the years her love "
			print "for her husband has faded a little but she also tells you "
			print "that she still felt like they had a strong bond. "
			print "You ask her if she had also spend the weekend in this house,"
			print " but she tells you that she was in their main house. "
			print "She likes it better because its interior equipment is far more luxuary."
			print " She seems to be appreciating her priveleged life a lot. "
			return inp_room
		elif choice == 'enter bathroom':
			print "As you enter the small bathroom attached to the bedroom "
			print "you see a big shower, a toilet and a baisin in there. "
			print "It seems like there is nothing connected to the case in here. "
			print "You decide to not waste any more time in here and instead "
			print "will go investigate somewhere else."
			return inp_room
		elif (choice == 'use fingerprint set with wife' or choice == 'use Fingerprint Set with Wife'):
			self.take_fingerprints(inp_room, 'Wife')
			return inp_room
		elif choice == 'leave':
			return 'entrance_corridor2'
			
		elif choice == 'inventory':
			self.call_inventory(inp_room)
			return inp_room			
			
		elif ('help' or 'Help') in choice:
			self.help(inp_room)
			return inp_room
		
		elif choice == 'map':
			map2.getmap_module(inp_room)
			return inp_room	
			
		elif ('use' and 'Fingerprint' and 'with') in choice and not ('Set' in choice):
			self.compare_fingerprints (inp_room, choice)
			return inp_room
		elif ('use' and 'fingerprint set' and 'with') in choice: 
			self.take_fingerprints_item(choice, inp_room)
			return inp_room
			
		elif 'use' in choice:
			print "This isnt the time to use that!"
			return inp_room
		else:
			error = self.inperror(inp_room)
			return error
class BathroomFirstFloor(Room):

	def enter(self):
		inp_room = 'bathroom_f1'
		print "You enter the bathroom, which looks pretty big and luxuary. "
		print "There is a bathtub, a shower and a baisin. "
		print "What do you want to do?"
		choice = raw_input(prompt)
		if choice == 'examine bathtub':
			print "You examine the bathtub and notice that "
			print "it doesn't only have two build in seats but also a "
			print "whirlpool-function. Taking a bath in there must be truly relaxing."
			return inp_room
		elif choice == 'examine shower':
			print "You look closely around the shower. It is a very big one "
			print "with a big shower head in the celing and a few smaller "
			print "nozzles built into the walls so the water would come "
			print "from all sides when someone takes a shower. Pretty fancy."
			return inp_room
		elif choice == 'examine baisin':
			print "The baisin looks expensive and is very big. "
			print "The tap has a sensor and the water comes out automaticly"
			print "when it notices a hand. "
			return inp_room
		elif choice == 'leave':
			return 'entrance_corridor2'
			
		elif choice == 'inventory':
			self.call_inventory(inp_room)
			return inp_room			
			
		elif ('help' or 'Help') in choice:
			self.help(inp_room)
			return inp_room
		
		elif choice == 'map':
			map2.getmap_module(inp_room)
			return inp_room	
			
		elif ('use' and 'Fingerprint' and 'with') in choice and not ('Set' in choice):
			self.compare_fingerprints (inp_room, choice)
			return inp_room
		elif ('use' and 'fingerprint set' and 'with') in choice: 
			self.take_fingerprints_item(choice, inp_room)
			return inp_room
			
		elif 'use' in choice:
			print "This isnt the time to use that!"
			return inp_room
		else:
			error = self.inperror(inp_room)
			return error
		
class ToiletFirstFloor(Room):

	def enter(self):
		inp_room = 'wc_f1'
		print "You enter the WC on the second floor."
		print "It looks like a normal WC. You see a toilet and a basin."
		print "What do you want to do?"
		choice = raw_input(prompt)
		if choice == 'examine toilet':
			print "You examine the toilet."
			print "It looks pretty normal and is probably"
			print "not related to the case."
			return inp_room
		elif choice == 'examine basin':
			print "You take a closer look at the basin."
			print "It is pretty big and the tap is golden with "
			print "lot of fancy features. It must have been expensive."
			return inp_room
		elif choice == 'leave':
			return 'entrance_corridor2'
			
		elif choice == 'inventory':
			self.call_inventory(inp_room)
			return inp_room			
			
		elif ('help' or 'Help') in choice:
			self.help(inp_room)
			return inp_room
		
		elif choice == 'map':
			map2.getmap_module(inp_room)
			return inp_room	
			
		elif ('use' and 'Fingerprint' and 'with') in choice and not ('Set' in choice):
			self.compare_fingerprints (inp_room, choice)
			return inp_room
		elif ('use' and 'fingerprint set' and 'with') in choice: 
			self.take_fingerprints_item(choice, inp_room)
			return inp_room
			
		elif 'use' in choice:
			print "This isnt the time to use that!"
			return inp_room
		else:
			error = self.inperror(inp_room)
			return error 
		
class Kidsbedroom1FirstFloor(Room):

	def enter(self):
		inp_room = 'bedroomkids1_f1'
		print "As you enter the kids bedroom you notice a bed,"
		print "a bookcase and a poster. What do you want to do?"
		choice = raw_input(prompt)
		if choice == 'examine bed:':
			print "The bed just big enough for one person and the bedding "
			print "has a printed on Star Wars motive. "
			print "It looks like it hasnt been touched in years."
			return inp_room
		elif choice == 'examine poster':
			print "The poster on the wall shows Yoda with his green light saber. "
			print "It says 'May the force be with you!'"
			return inp_room
		elif choice == 'examine bookcase':
			return 'saferoom_f1'
		elif choice == 'leave':
			return 'entrance_corridor2'
			
		elif choice == 'inventory':
			self.call_inventory(inp_room)
			return inp_room			
			
		elif ('help' or 'Help') in choice:
			self.help(inp_room)
			return inp_room
		
		elif choice == 'map':
			map2.getmap_module(inp_room)
			return inp_room	
			
		elif ('use' and 'Fingerprint' and 'with') in choice and not ('Set' in choice):
			self.compare_fingerprints (inp_room, choice)
			return inp_room
		elif ('use' and 'fingerprint set' and 'with') in choice: 
			self.take_fingerprints_item(choice, inp_room)
			return inp_room
			
		elif 'use' in choice:
			print "This isnt the time to use that!"
			return inp_room
		else:
			error = self.inperror(inp_room)
			return error
class SaferoomFirstFloor(Room):

	def enter(self):
		global code_entered
		global locket_pickup
		if code_entered == False:
			print "You examine the bookcase closely and notice that it is hiding a secret door leading to some kind of safe room. You find a key pad behind a book called 'Hitchhikers guide to the Galaxy'. It seems that you need to enter a 4 digit code to open the secret door. Use the command 'enter' to enter the code."
			choice = raw_input(prompt)
			if choice == 'enter 4062':
				print "The code must have been right."
				print "The door swings open and you can enter the safe room."
				code_entered = True
				return 'saferoom_f1'
			elif 'enter' in choice:
				print "It seems that the code was wrong. The door doesnt open."
				return 'saferoom_f1'
			elif choice == 'leave':
				return 'bedroomkids1_f1'
				
			elif choice == 'inventory':
				self.call_inventory(inp_room)
				return inp_room			
				
			elif ('help' or 'Help') in choice:
				self.help(inp_room)
				return inp_room
			
			elif choice == 'map':
				map2.getmap_module(inp_room)
				return inp_room	
				
			elif ('use' and 'Fingerprint' and 'with') in choice and not ('Set' in choice):
				self.compare_fingerprints (inp_room, choice)
				return inp_room
			elif ('use' and 'fingerprint set' and 'with') in choice: 
				self.take_fingerprints_item(choice, inp_room)
				return inp_room
				
			elif 'use' in choice:
				print "This isnt the time to use that!"
				return inp_room
			else:
				error = self.inperror('saferoom_f1')
				return error
		elif code_entered == True and locket_pickup == False:
			print "You enter the safe room and you see..."
			print "Nothing."
			print "You look around closely and in one of the corners "
			print "you find a locket on a broken necklace. As you look inside,"
			print " you see a picture of the victim. "
			print "The locket has been added to your inventory"
			print "You go back into the kids bedroom. "
			locket_pickup = True
			item_room = self.add_inventory('Locket', 'bedroomkids1_f1')
			return item_room
		elif code_entered == True and locket_pickup == True:
			print "You enter the safe room and you see..."
			print "Nothing."
			print "You go back into the kids bedroom. "
			return 'bedroomkids1_f1'
		else:
			print "You broke the game. Bravo. "
			

class Map(object):

	RoomList = {
	'welcome_screen': WelcomeScreen(),
	'entrance_corridor': EntranceCorridor(),
	'entrance_corridor2': EntranceCorridor2(),
	'wc_eg': ToiletEG(),
	'livingrm1_eg': Livingroom1EG(),
	'diningrm_eg': DiningroomEG(),
	'kitchen_eg': KitchenEG(),
	'livingrm2_eg': Livingroom2EG(),
	'office_eg': OfficeEG(),
	'corridor_bs': CorridorBasement(),
	'laundry_bs': LaundryBasement(),
	'sauna_bs': SaunaBasement(),
	'storage1_bs': Storage1Basement(),
	'bedroom_f1': BedroomFirstFloor(),
	'bathroom_f1': BathroomFirstFloor(),
	'wc_f1': ToiletFirstFloor(),
	'bedroomkids1_f1': Kidsbedroom1FirstFloor(),
	'saferoom_f1': SaferoomFirstFloor(),
	'guestroom1_f1': Guestroom1FirstFloor(),
	'solve_screen': SolveScreen(),
	}
	
	
	def __init__(self, start_room):
		self.start_room = start_room
		
	def next_room(self, room_name):
		#print "Debug: Next room"
		#print "next scene"
		#print "current scene name %s" % room_name
		print ""
		room_list = self.RoomList[room_name]
		#print "dict scene is %s" %room_list
		return room_list

	def opening_room(self):
		Map.start_room = opening_room
		current_room.enter()

a_map = Map('welcome_screen')
a_game = Engine(a_map)
a_game.play()