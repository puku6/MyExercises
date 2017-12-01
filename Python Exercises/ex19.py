# define function "cheese_and_crackers"
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	#just print using value cheese_count
	print "You have %d cheeses!" % cheese_count
	#just print using value boxes_of_crackers
	print "You have %d boxes of crackers!" % boxes_of_crackers
	#just print 
	print "Man thats enought for a Party!"
	#just print with linefeed
	print "Get a blanket.\n"
	
# just print
print "We can just give the function numbers directly:"
# using function cheese_and_crackers while giving it the values directly
cheese_and_crackers(20, 30)
	
# just print
print "OR we can use variables from our script:"
# defining the variable amount_of_cheese to put inside of function "cheese_and_crackers"
amount_of_cheese = 10
# defining the variable amount_of_crackers to put inside of function "cheese_and_crackers"
amount_of_crackers = 50
# using variables "amount_of_cheese" and "amount_of_crackers" as "cheese_count" and "boxes_of_crackers" in function "cheese_and_crackers"
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# just print
print "We can even do math inside too:"
#use function "cheese_and_crackers" while finding the variables through math
cheese_and_crackers(10 + 20, 5 + 6)

#just print
print "And we can comine the two, variables and math:"
# combine math with the variables "amount_of_cheese" and "amount_of_crackers" to represent "cheese_count" and "boxes_of_crackers"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)