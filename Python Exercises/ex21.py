def add(a,b):
	print "ADDING %d to %d" % (a,b)
	return a + b
	
def subtract(a, b): 
	print "SUBTRACTING %d - %d" % (a,b)
	return a - b
	
def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a,b)
	return a * b 

def divide (a, b):
	print "DIVIDING %d / %d" % (a,b)
	return a / b
	

print "Let's do some math with just functions!"

age = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide (100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
# the same as age + height - weight * (iq/20) = 35+74-180*(50/2)
print "that becomes: ", what, "Can you do it by hand?"
print "here comes my own puzzle"
puzzle = divide(multiply((subtract(age, weight)),(add(height, iq))),2)
print " = ", puzzle
print "and now to the normal calculation"
puzzle_easy = divide(multiply(add(1,2),4),5)
print " = ", puzzle_easy 
