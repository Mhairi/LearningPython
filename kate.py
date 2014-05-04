start = 1000

counter = start - 17
number = input("Subtract 17 from %d: " % start) 

if counter==number:
    print "\n" * 80
    print "Correct."
    counter = counter - 17
else:
    print "\n" * 80
    print "That was terrible, let's try again from 1000."
    counter = 983
        

number = input("Subtract 17 from that: ") 

if counter==number:
    print "\n" * 80
    print "Correct."
    counter = counter - 17
else:
    print "\n" * 80
    print "That was terrible, let's try again from 1000."
    counter = 983
    
number = input("Subtract 17 from that: ") 

if counter==number:
    print "\n" * 80
    print "Correct."
    counter = counter - 17
else:
    print "\n" * 80
    print "That was terrible, let's try again from 1000."
    counter = 983
