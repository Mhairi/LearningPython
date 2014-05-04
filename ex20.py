from sys import argv # looks into sys and imports arguments fro argv

script, input_file = argv # these arguments are the script itself, and another file named input_file

def print_all(f): # defines a function named print_all
    print f.read() # in this function, we take f and run the function "read" on it.
    
def rewind(f): # defines a function named rewind.
    f.seek(0) # runs the function seeko n it

def print_a_line(line_count, f): # defines a function print_a_line
    print line_count, f.readline() # prints the variable line_count, and runs the readline command on it
    
current_file = open(input_file) # this is the important part where the variable current_file is defined as the contents of input_file (which was typed in as an argument"

print "First let's print the whole file:\n" # prints the text

print_all(current_file) # does what the function does

print "Now let's rewind, kind of like a tape." # prints the text

rewind(current_file) # does what the function does

print "Let's print three lines:"

current_line = 1 # counter, global level
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

