from sys import argv

script, filename = argv

target = open(filename)

print "Here's the file %s you just created" % filename
print target.read()
target.close()
