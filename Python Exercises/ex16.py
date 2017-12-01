# import argv
from sys import argv

# define input from argv
script, filename = argv

#print using string filename
print "We're going to erase %r." % filename

# just print
print "If you don't want that, hit CTRL-C (^C)."

# just print
print "If you do want that, hit RETURN."

# prompting input using promp "?"
raw_input("?")

# just print 
print "Opening the file..."

# defining target as open file "filename" using writing mode
target = open(filename, 'w')

# just print
print "Truncating the file. Goodbye!"

# erasing the data in target file; not necessary because "w-mode" already erases the data
# target.truncate()

# just print
print "Now I'm going to ask you for three lines."

# prompting raw input using prompt "line 1:"
line1 = raw_input("line 1: ")

# prompting raw input using prompt "line 2:"
line2 = raw_input("line 2: ")

# prompting raw input using prompt "line 3:"
line3 = raw_input("line 3: ")

# just print
print "I'm going to write these to the file."

# writing lines into target file using strings to shorten and escape Sequence linefeed
target.write("%s\n%s\n%s\n" %(line1, line2, line3))

# just print
print "And finally, we close it."

# closing target file
target.close()