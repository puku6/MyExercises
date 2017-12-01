people = 20
cats = 30
dogs = 15

# The if-statement runs the code under it, but only IF the statement is true...
# ...otherwise it will just skip it.
if people < cats:
	# The 4 spaces/ 1 tab is needed so it is recognized as a related code
	# if there is not at least 1 space, it will create an IdentationError
	print "Too many cats! The world is doomed!"
	
if  people > cats:
	print "Not many cats! The world is saved!"

if people < dogs:
	print "The world is drooled on!"
	
if people > dogs:
	print "The world is dry!"
	
dogs += 5

if people >= dogs:
	print "People are greater than or equal to dogs."

if people <= dogs: 
	print "People are less than or equal to dogs."
	
if people == dogs: 
	print "People are dogs."
	
cats -= 10
if people == dogs and  people == cats :
	print "People are CATDOGS!"
cats += 5
dogs += 5
if people != cats or people > dogs :
	print "People arent cats... or it's drooled world... or both? "