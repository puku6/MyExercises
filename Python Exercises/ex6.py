# defining a scentence x (string) and a variable (which is also used as string)
 x = "There are %d types of people." % 10
# defining string binary
  binary = "binary"
# defining string do_not
  do_not = "don’t"
# defining string y and insert strings binary and do_not
  y = "Those who know %s and those who %s." % (binary, do_not)  
# print string x 
 print x
# print string y
  print y  
# print string x inside of a string
 print "I said: %r." % x
# printing string y inside of a string
   print "I also said: '%s'." % y   
# defining hilarious with a keyword
   hilarious = False
# defining joke_evaluation with another string/keyword inside
   joke_evaluation = "Isn’t that joke so funny?! %r"   
 # printing  strings
 print joke_evaluation % hilarious   
# defining string w
   w = "This is the left side of..."
# defining string e
   e = "a string with a right side."
# printing strings w and e (not inside, but after each other)
print w + e  
