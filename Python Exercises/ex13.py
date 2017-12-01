from sys import argv
script, car = argv
print "The script is called:", script
print "Your favorite car is a ", car
print "or which is it?"
answer = raw_input()
print "Oh, so your favorite car is a " % answer
