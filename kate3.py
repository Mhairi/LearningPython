start = 2023

counter = start - 17
print "Please count backwards from 2023 to 0 in 17-step sequences: "
    
while counter != 0:
    while True:
        try:
            number = int(raw_input(">")) or "0"
            break
        except:
            print "Only numbers are valid."
        
    if counter == number:
        print "\n" * 80
        print "Next: "
        counter = counter - 17
    else:
        print "\n" * 80
        print "Stop - mistake - start over at 2023 please: "
        counter = 2006

print "Please inform the experimenter that you have finished with the task."
raw_input("Press enter to quit.")
