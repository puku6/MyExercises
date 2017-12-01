#import module argv
from sys import argv
#define input from argv
script, input_file = argv

#define function print_all... 
def print_all(f):
#...as a print of a file
	print f.read()
#define function rewind...
def rewind(f):
#...to seek the byte at position 0
	f.seek(0)

#define print_a_line
def print_a_line(line_count, f):
#by printing the line count first, then the associated line
	print line_count, f.readline()

#now, transfer the input string from argv into the opened file
current_file = open(input_file)

#just print with a linefeed
print "First, let's print the whole file:\n"
#print ALL of the file using print_all function
print_all(current_file)

#just print
print "Now let's rewind, kind of like a tape."
#use function rewind(f) to return to the start of our current file
rewind(current_file)

#just a print
print "Let's print three lines"

#set the current line to read as line =1 
current_line = 1
#use function print_a_line to print the current line 
print_a_line(current_line, current_file)

#add one to our current line -> =2
current_line = current_line + 1
#use function print_a_line to first print the line count (2) and then to print our new current line 
print_a_line(current_line, current_file)

#add one to our current line -> =3
current_line = current_line + 1
#use function print_a_line to first print the line count (3) and then to print the newest current line 
print_a_line(current_line, current_file)