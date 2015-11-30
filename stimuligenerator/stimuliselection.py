import csv
from random import randint, seed

seed(0) #Set our random seed to 0

stimulifile = open('stimuli.csv', 'rb') #Open csv file
stimulicsv = csv.reader(stimulifile) #csv file is a csv.reader object

stimuliinitial = [] #stimuli is an empty array

for line in stimulicsv:
    stimuliinitial.append(line) #append each line in the csv reader object to the stimuli

#Conditions for selecting stimuli

#for one condition:
#Sum of group > sum of self more condition
#self within group more < self within the self more
#other within group more > other within the self more

#self != other X
#ignore 1 coin difference (for single stimuli) X

#for the other condition:
#sum of group > sum of self more condition
#self within group more > self within self more
#other within group more < other within self more

#self != other X
#ignore 1 coin difference (for single stimuli) X

#we first get rid of all the stimuli with 1 coin difference:

stimuli2ndpass = []

for i in range(0, len(stimuliinitial)):
    if (int(stimuliinitial[i][0]) != int(stimuliinitial[i][1])+1) & (int(stimuliinitial[i][0]) != int(stimuliinitial[i][1])-1) :
        stimuli2ndpass.append(stimuliinitial[i])

        
#Next, we add all the options that are the reverse of the initial options
stimuli = []

for i in range(0,len(stimuli2ndpass)):
    stimuli.append(stimuli2ndpass[i])
    stimuli.append(stimuli2ndpass[i][::-1])


#What we want to do is to populate an array of acceptable *pairs* of stimuli
#To do so, we are going to randomly select from our array of stimuli

acceptablestimuli1 = [] #We will populate this array (self vs. group with self less within the group option)

while len(acceptablestimuli1) < 50: #While there are less than 10 entries in this array, do the following:
    optiona = stimuli[randint(0,len(stimuli)-1)] #This randomly select one option from all our possible stimuli
    optionb = stimuli[randint(0,len(stimuli)-1)] #This too
    if (int(optiona[0]) > int(optionb[0])) & (int(optiona[1]) < int(optionb[1])): #if the self gets less in the group option
        if (int(optiona[0])+int(optiona[1])) < (int(optionb[0]) + int(optionb[1])):
            acceptablestimuli1.append([[int(optiona[0]),int(optiona[1])], [int(optionb[0]),int(optionb[1])]])
        else:
            pass
    else:
        pass 

acceptablestimuli2 = [] #We will populate this array (self vs. group with self more within the group option)

while len(acceptablestimuli2) < 50: #While there are less than 10 entries in this array, do the following:
    optiona = stimuli[randint(0,len(stimuli)-1)] #This randomly select one option from all our possible stimuli
    optionb = stimuli[randint(0,len(stimuli)-1)] #This too
    if (int(optiona[0]) < int(optionb[0])) & (int(optiona[1]) > int(optionb[1])): #if the self gets *more* in the group option
        if (int(optiona[0])+int(optiona[1])) < (int(optionb[0]) + int(optionb[1])):
            acceptablestimuli2.append([[int(optiona[0]),int(optiona[1])], [int(optionb[0]),int(optionb[1])]])
        else:
            pass
    else:
        pass 


selfvsgroupstimuli = open('selfvsgroupstimuli.csv','wb') #opens this file for writing

selfvsgroupstimuliwriter = csv.writer(selfvsgroupstimuli) #creates a csv.writer object

header1 = ['Self','Group (self less)'] #our first header
selfvsgroupstimuliwriter.writerow(header1) #write the header
for line in acceptablestimuli1: #write each line in acceptable stimuli
    selfvsgroupstimuliwriter.writerow(line)
    
header2 = ['Self','Group (self more)']
selfvsgroupstimuliwriter.writerow(header2)
for line in acceptablestimuli2: #write each line in acceptable stimuli
    selfvsgroupstimuliwriter.writerow(line)

stimulifile.close()
selfvsgroupstimuli.close()

