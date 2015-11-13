import stimuligenerator as sg
import csv

#We need to generate 40 stimuli for each of the comparisons.

stimuliarray = []

stimuliarray.append(['Self favoring', '','Other favoring',''])
for i in xrange(1,41): #40 for self vs. other
    stimuliarray.append(sg.GenerateSelf()+sg.GeneratePartner())   
    
stimuliarray.append(['Self favoring', '','Group favoring',''])
for i in xrange(1,41): #40 for self vs. group 
    stimuliarray.append(sg.GenerateGroupvsSelf()[0]+sg.GenerateGroupvsSelf()[1])

stimuliarray.append(['Other favoring','', 'Group favoring',''])
for i in xrange(1,41): #40 for other vs. group 
    stimuliarray.append(sg.GenerateGroupvsPartner()[0] + sg.GenerateGroupvsPartner()[1])
                  
   
file = open('stimuli.csv', 'wb')
csvfile = csv.writer(file)

for row in stimuliarray:
    csvfile.writerow(row)
    
file.close()