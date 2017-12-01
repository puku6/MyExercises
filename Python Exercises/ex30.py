# sets "people" to 65
people = 65
# sets "cars" to 40
cars = 65
# sets "trucks" to 15
trucks = 65

# if the statement "there are more cars than people" is true...
if cars > people:
	# print this line
	print "We should take the cars."

# otherwise, if the statement "there are less cars than people" is true...
elif cars < people: 
	# print this 
	print "We should not take the cars."
# if its neither (that means cars = people)...
else:
	# print this.
	print "We can't decide."

# same game here: more trucks than cars 
if trucks > cars:
	#print this
	print "Maybe we could take the trucks."

# else if less trucks than cars 
elif trucks < cars: 
	# print this
	print "Maybe we could take the trucks."
# otherwise 
else:
	# print this 
	print "We still can't decide."
	
# if there are more people than trucks 
if people > trucks:
	print "Alright, let's just take the trucks."
# otherwise (this times, that means less people than trucks OR people equals trucks)
else: 
	print "Fine, let's stay home then."
	
# as explained, elis is "else if"; if the "if-statement" is not true...
# the elif statement is checked. If it's true, it will be executed.

# else on the otherhand, is what happens if all statements above (all if- and elif-statements)...
# are False, only THEN it is executed.