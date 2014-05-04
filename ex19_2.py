amount = int(raw_input("How many sausages would you like to start with? "))
print "You have chosen to start with %d sausages. A wise choice." % amount

def sausage():
    global amount
    return amount

amount += 1

raw_input("""
Press enter for another sausage, or press CTRL-C to stop the sausages.
""")
print "The sausage counter now reads %d sausages" % sausage()

amount += 1

raw_input("""
Press enter for another sausage, or press CTRL-C to stop the sausages.
""")
print "The sausage counter now reads %d sausages" % sausage()

amount += 1

raw_input("""
Press enter for another sausage, or press CTRL-C to stop the sausages.
""")
print "The sausage counter now reads %d sausages" % sausage()

amount += 1

raw_input("""
Press enter for another sausage, or press CTRL-C to stop the sausages.
""")
print "The sausage counter now reads %d sausages" % sausage()

print "\bToo many sausages. Cannot compute."
