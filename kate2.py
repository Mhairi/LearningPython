import sys

start = 1000

counter = start - 17
print "Let's start from 1000."
    
for attempts in range (0, 10):

    number = raw_input("Subtract 17 from that: ") or 0
    number = int(number)
    if counter==number:
        print "\n" * 80
        print "Correct."
        counter = counter - 17
    else:
        print "\n" * 80
        print "That was terrible, let's try again from 1000."
        counter = 983
        
sys.exit()
