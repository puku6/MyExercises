def loop_number( number_add, number_max):
	i = 4 
	numbers  = []

	for i in range (4, number_max):
		print "At the top i is %d" % i 
		numbers.append(i)
	
		# using this incrementer makes the code confusing.
		# it doesnt use the custom steps (number_add) for appending..
		#i = i + number_add
		print "Numbers now: ", numbers
		# ...but only for calling the bottom i. 
		print "At the bottom i is %d" % i
		
	return numbers
numbers = loop_number(3, 25)
	
	
print "The numbers: "

for num in numbers:
	print num
	
numbers = loop_number(7, 34)
	
	
print "The new numbers: "

for num in numbers:
	print num