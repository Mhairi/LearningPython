from sys import argv # from system, import the argument variables in argv

script = argv # these are the two argument variables

filename = raw_input ("Please enter the exact name of the file you would like to open (e.g., text.txt)" )
txt = open(filename) # takes what the user typed out in the filename argument, and opens the file, defined as the varible txt

print "Here's your file %r:" % filename # prints text, and filename
print txt.read() # calls the function read() on txt, and prints that
