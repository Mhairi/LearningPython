from random import randint, seed

seed = (0)

def GenerateSelf(): #Function to generate two numbers, self higher
    selfanswer = False #Start condition for loop
    while selfanswer == False: #As long as we haven't found two numbers that fit our criteria
        numberone = randint(1,100) #First number is a random number from 1-100
        numbertwo = randint(1,100) #Second number is a random number from 1-100
        if numberone == numbertwo:
            selfanswer = False #If the two numbers are the same, maintain False to let the loop continue
        else:
            #If the two numbers are different, we sort them in descending order (so the higher value for the
            #self is first)
            selfanswer = sorted([numberone,numbertwo], reverse = True) 
            return selfanswer #Returns our two integer array
            
#Exact same logic as above, except we do not sort in reverse order (so the 2nd number, for partner, is higher)
def GeneratePartner():
    partneranswer = False
    while partneranswer == False: 
        numberone = randint(1,100)
        numbertwo = randint(1,100)
        if numberone == numbertwo:
            partneranswer = False
        else:
            partneranswer = sorted([numberone,numbertwo])
            return partneranswer
            
#Now we write a GenerateGroupvsPartner function that returns an array with two sub-arrays. The first is two group-favoring
#answers (their sum is larger than the sum of the 2nd array numbers). The 2nd array numbers favor the partner.
def GenerateGroupvsPartner():
    groupanswer = False #This remains false until we get the answer we want
    while groupanswer == False: #Keep looping until we get the answer we want
        firstarray = [randint(1,100), randint(1,100)] #First array is two random numbers
        firstarraysum = firstarray[0] + firstarray[1]
        secondarray = GeneratePartner() #Second array is two numbers where the partner gets more
        secondarraysum = secondarray[0] + secondarray[1]
        if firstarraysum <= secondarraysum:
            groupanswer = False #We don't meet the criteria, so keep looping
        else:
            return [firstarray, secondarray]
        
def GenerateGroupvsSelf():
    groupanswer = False
    while groupanswer == False:
        firstarray = [randint(1,100), randint(1,100)] 
        firstarraysum = firstarray[0] + firstarray[1]
        secondarray = GenerateSelf() #Second array is two numbers where the partner gets more
        secondarraysum = secondarray[0] + secondarray[1]
        if firstarraysum <= secondarraysum:
            groupanswer = False #We don't meet the criteria, so keep looping
        else:
            return [firstarray, secondarray]
            
def GenerateSelfvsPartner():
    return [GenerateSelf(),GeneratePartner()]