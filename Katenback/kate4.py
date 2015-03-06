start = 2023 # starting number
increment = 17 # increment value
mistakes = 0 # mistake counter
lowcounter = start - increment # score counter
counter = start - increment # counter for the function
print "Please count backwards from 2023 to 0 in 17-step sequences: "
    
while counter != 0: # while counter is not zero
    while True:
        try: # tests to see if participant's input is a number
            number = int(raw_input(">"))
            break
        except: # if not
            print "Only numbers are valid."
        
    if counter == number: # if participant types in the correct answer
        print "\n" * 80 # spacer to clear screen
        print "Next: " 
        counter = counter - increment # updates counter
        if counter < lowcounter: # tests to see if this is participant's best score
            lowcounter = counter # if so, takes note of that value
    elif number == 99999: # super secret magic code
        print "The participant made %d mistakes." % mistakes
        print "The participant's lowest number was %d." % (lowcounter + increment)
    else:
        print "\n" * 80 # spacer to clear screen
        print "Stop - mistake - start over at 2023 please: "
        counter = start - increment # resets counter
        mistakes = mistakes + 1 # adds one to mistake counter

print "Please inform the experimenter that you have finished with the task."
raw_input("Press enter to quit.")
