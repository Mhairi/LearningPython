from sys import argv # from system, import the argument variables in argv

script, filename = argv # these are the two argument variables

txt = open(filename) # takes what the user typed out in the filename argument, and opens the file, defined as the varible txt

print "Here's your file %r:" % filename # prints text, and filename
print txt.read() # calls the function read() on txt, and prints that

print "Type the filename again:" # prints the text
file_again = raw_input("> ") # asks the user for raw input, and defines that as file_again

txt_again = open(file_again) # opens what the user typed in file_again, and defines it at txt_again

print txt_again.read() # calls the function read on txt_again
