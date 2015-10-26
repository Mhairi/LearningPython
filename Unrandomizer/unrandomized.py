#We want the 1st column to be the participant's ID, followed by 5 x 15 columns:
#Raw choices (1-4) arranged in actual completion order.
#Self amount arranged in actual completion order.
#Other amount arranged in actual completion order.
#Cumulative sum across the 15 trials.
#Cumulative difference across the 15 trials.

#What we get is the first column as the participant's ID, followed by 16 columns:
#Participants choices for Q1-Q15.
#16th column showing order these choices were presented in.

#Import packages
import csv
import numpy as np

#Opening our dataset
original_data_file = open('choicesnonordered.csv', 'rb') #Opens a file
original_data_csv = csv.reader(original_data_file) #Reads it as a .csv object
original_data_header = original_data_csv.next() #Reads the header as the first line
original_data = [] #Empty array for our data

for row in original_data_csv: #Append each row
    original_data.append(row)

#original_data = np.array(original_data) #Re-type original data to an np.array.

#Opening our dataset with the random orderings
order_key_file = open('idsandorders.csv','rb')
order_key_csv = csv.reader(order_key_file)
order_key = {} #Dictionary object for our IDs and order

for row in order_key_csv: #For each row in the csv
    row[1] = row[1].split('|') #Split the string up by the "|" character, as it is in the data
    for i in xrange(0,len(row[1])): #For each of the 15 question numbers in the row
        row[1][i] = int(row[1][i].replace('Q','')) #Replace "Q" with nothing, and convert it to an integer.
    #print row[1] #Print the row, to debug.
    order_key[row[0]] = row[1] #Adds a dictionary entry with the ID (row[0]) as the key, and the order (row[1]) as the value.


#We need to first convert Ps un-randomized choices into values (before we can rearrange them).

#Let's make a 15x4 array to store the values of each choice for the self.
self_values = [[0.2,0.25,0.15,0.05],
                 [0.17,0.22,0.12,0.02],
                 [0.15,0.2,0.1,0],      
                 [0.25,0.3,0.2,0.1],
                 [0.31,0.34,0.24,0.14],
                 [0.26,0.31,0.23,0.11],
                 [0.13,0.21,0.12,0.02],
                 [0.23,0.26,0.19,0.05],
                 [0.1,0.15,0.05,0.02],
                 [0.22,0.26,0.17,0.03],
                 [0.15,0.19,0.1,0.01],
                 [0.25,0.3,0.2,0.1],
                 [0.18,0.22,0.13,0.03],
                 [0.13,0.18,0.11,0.04],
                 [0.31,0.37,0.25,0.16]]
#We call these back later with self[i][j]

#Let's make another 15x4 array to store values of each choice for the partner.
other_values = [[0,0.1,0.25,0.3],
                [0,0.07,0.22,0.27],
                [0,0.05,0.2,0.25],
                [0.05,0.15,0.3,0.35],
                [0.09,0.19,0.35,0.39],
                [0.04,0.16,0.31,0.36],
                [0,0.07,0.32,0.26],
                [0,0.13,0.27,0.34],
                [0,0.03,0.15,0.16],
                [0,0.07,0.27,0.3],
                [0,0.05,0.21,0.23],
                [0.05,0.15,0.3,0.35],
                [0,0.09,0.22,0.28],
                [0,0.09,0.21,0.23],
                [0.12,0.23,0.36,0.44]]

#Here we do our math stuff. Basically, It'll be operations involving multiples of 15.

end_data = original_data #This will end up being a 250++x61 array.
end_data = [x + [0] * 30  for x in end_data] #This uses list comprehension to loop through all 
#rows of end_data, and creates 30 new columns

selfglobaliter = 16
otherglobaliter = 31
questionglobaliter = 0

#We want to loop through indices 1 to 15, and place values in indices 16-30 (self-values), (other-values).
for row in end_data: #Loop through each row

    selfiter = selfglobaliter #These call on our global variables, and will serve as indices.
    otheriter = otherglobaliter
    questioniter = questionglobaliter
    
    for i in row[1:]: #For all the is in each row, but skipping the first one (Participant ID)
        if i == '1': #This series of if statements checks to see what participants' choices were.
            row[selfiter] = self_values[questioniter][0] #For the current row, the self_value is the 0th index (first choice)
            row[otheriter] = other_values[questioniter][0] #Of the that question in the self_values array              
        elif i == '2':
            row[selfiter] = self_values[questioniter][1]
            row[otheriter] = other_values[questioniter][1]            
        elif i == '3':
            row[selfiter] = self_values[questioniter][2]
            row[otheriter] = other_values[questioniter][2]          
        elif i == '4':
            row[selfiter] = self_values[questioniter][3]
            row[otheriter] = other_values[questioniter][3]       

        selfiter += 1 #These iterators advance our indices
        otheriter += 1
        questioniter += 1

end_data = np.array(end_data)

#We separate the data here to make things simpler, and will join t back later
ids = end_data[::,0]
choices = end_data[::,1:16]
self_data = end_data[::,16:31]
other_data = end_data[::,31:46]

choices = np.column_stack((ids,choices)) #Adds ids to the first row
self_data = np.column_stack((ids,self_data))
other_data = np.column_stack((ids,other_data))


unrandomized_choices = []
unrandomized_self_data = []
unrandomized_other_data = []

for row in choices:
    ordered_index = order_key[row[0]] #Returns the indices of the un-random order (the order P's saw the questions)
    ordered_row = [None]*(len(row)) #Pre-initializes an empty array (so we can use the indices).
    ordered_row[0] = row[0] #First column of the ordered_row is P's ID.
    for i in xrange(0, len(row)-1): #For each response (but we have to bear in mind that index 0 is the P's ID), we "reposition" it to the right place using the un-randomized index.
        ordered_row[i+1] = row[ordered_index[i]] #We + 1 because the ID is in the first "column", so the indices we want range from 1-15 vs. 0-14 with the ordered_index.
    unrandomized_choices.append(ordered_row)
    
for row in self_data:
    ordered_index = order_key[row[0]] #Returns the indices of the un-random order (the order P's saw the questions)
    ordered_row = [None]*(len(row)) #Pre-initializes an empty array (so we can use the indices).
    ordered_row[0] = row[0] #First column of the ordered_row is P's ID.
    for i in xrange(0, len(row)-1): #For each response (but we have to bear in mind that index 0 is the P's ID), we "reposition" it to the right place using the un-randomized index.
        ordered_row[i+1] = row[ordered_index[i]] #We + 1 because the ID is in the first "column", so the indices we want range from 1-15 vs. 0-14 with the ordered_index.   
    unrandomized_self_data.append(ordered_row)
    
for row in other_data:
    ordered_index = order_key[row[0]] #Returns the indices of the un-random order (the order P's saw the questions)
    ordered_row = [None]*(len(row)) #Pre-initializes an empty array (so we can use the indices).
    ordered_row[0] = row[0] #First column of the ordered_row is P's ID.
    for i in xrange(0, len(row)-1): #For each response (but we have to bear in mind that index 0 is the P's ID), we "reposition" it to the right place using the un-randomized index.
        ordered_row[i+1] = row[ordered_index[i]] #We + 1 because the ID is in the first "column", so the indices we want range from 1-15 vs. 0-14 with the ordered_index.   
    unrandomized_other_data.append(ordered_row)


unrandomized_sum_data = []
unrandomized_diff_data = []

rowiter = 0

#We loop through all the rows in our unrandomized dataset, and calculate the sum and difference
for row in unrandomized_self_data: #Loop through each row
    tempsum = [row[0]] #Creates a temporary array and adds IDs
    tempdiff = [row[0]]
    sumdiffiter = 1 #Resets the iterator
    for i in row[1:]: #For all the is in each row, but skipping the first one (Participant ID)
        tempsum.append(float(unrandomized_self_data[rowiter][sumdiffiter]) + float(unrandomized_other_data[rowiter][sumdiffiter]))
        tempdiff.append(float(unrandomized_self_data[rowiter][sumdiffiter]) - float(unrandomized_other_data[rowiter][sumdiffiter]))
        sumdiffiter += 1
    unrandomized_sum_data.append(tempsum) #Adds the current row to the array
    unrandomized_diff_data.append(tempdiff)
    rowiter += 1


#We convert these arrays to np.array to make some operations simpler
unrandomized_choices = np.array(unrandomized_choices)
unrandomized_self_data = np.array(unrandomized_self_data)
unrandomized_other_data = np.array(unrandomized_other_data)
unrandomized_sum_data = np.array(unrandomized_sum_data)
unrandomized_diff_data = np.array(unrandomized_diff_data)

unrandomized_self_data = unrandomized_self_data[::,1:16]
unrandomized_other_data = unrandomized_other_data[::,1:16]
unrandomized_sum_data = unrandomized_sum_data[::,1:16]
unrandomized_diff_data = unrandomized_diff_data[::,1:16]

#Joining all the data
all_unrandomized_data = np.column_stack((unrandomized_choices,unrandomized_self_data,unrandomized_other_data,unrandomized_sum_data,unrandomized_diff_data))


#We need to write a bunch of loops for cumulative sum
cumulative_self = []
cumulative_other = []
cumulative_sum = []
cumulative_diff = []

rowiterator = 0

for row in unrandomized_self_data:
    temprow = []
    for i in xrange(0,len(row)):
        if i == 0:            
            temprow.append(row[i])
        else:
            temprow.append(float(row[i]) + float(temprow[i-1]))
    cumulative_self.append(temprow)
    rowiterator += 1

#OK THIS IS THE WEIRDEST THING. IF YOU USE THE INDEX FOR THE LAST ROW IN A LIST (e.g., cumulative_sum[309] in this case), IT REFERS TO ALL THE
#ROWS IN THE LIST

for row in unrandomized_other_data:
    temprow = []
    for i in xrange(0,len(row)):
        if i == 0:            
            temprow.append(row[i])
        else:
            temprow.append(float(row[i]) + float(temprow[i-1]))
    cumulative_other.append(temprow)
    rowiterator += 1

for row in unrandomized_sum_data:
    temprow = []
    for i in xrange(0,len(row)):
        if i == 0:            
            temprow.append(row[i])
        else:
            temprow.append(float(row[i]) + float(temprow[i-1]))
    cumulative_sum.append(temprow)
    rowiterator += 1

for row in unrandomized_diff_data:
    temprow = []
    for i in xrange(0,len(row)):
        if i == 0:            
            temprow.append(row[i])
        else:
            temprow.append(float(row[i]) + float(temprow[i-1]))
    cumulative_diff.append(temprow)
    rowiterator += 1


#We convert these arrays to np.array to make some operations simpler
cumulative_self_data = np.array(cumulative_self)
cumulative_other_data = np.array(cumulative_other)
cumulative_sum_data = np.array(cumulative_sum)
cumulative_diff_data = np.array(cumulative_diff)

cumulative_self_data = cumulative_self_data[::,0:16]
cumulative_other_data = cumulative_other_data[::,0:16]
cumulative_sum_data = cumulative_sum_data[::,0:16]
cumulative_diff_data = cumulative_diff_data[::,0:16]

#Joining all the data
all_cumulative_data = np.column_stack((unrandomized_choices,cumulative_self_data,cumulative_other_data,cumulative_sum_data,cumulative_diff_data))


ids = ['ParticipantID'] 
choices = range(1,16) #Creates an array from 1 to 15
selfamounts = range(1,16) 
otheramounts = range(1,16)
sumamounts = range(1,16)
diffamounts = range(1,16)

choices = ["Choice%s" % x for x in choices] #Uses list comprehension to rename each item in the array "Choice%s" % x.
selfamounts = ["SelfAMount%s" % x for x in selfamounts] 
otheramounts = ["OthAmount%s" % x for x in otheramounts]
sumamounts = ["SumAmount%s" % x for x in sumamounts]
diffamounts = ["DiffAmount%s" % x for x in diffamounts]

final_header = ids + choices + selfamounts + otheramounts + sumamounts + diffamounts
cumulative_header = ids + choices + selfamounts + otheramounts + sumamounts + diffamounts


unrandomized_sharing_game_file = open('unrandomized.csv', 'wb') #Opens a file for writing.
unrandomized_sharing_game_csv = csv.writer(unrandomized_sharing_game_file) #Creates a new csv object that we can write to.

unrandomized_sharing_game_csv.writerow(final_header)

for row in all_unrandomized_data:
    unrandomized_sharing_game_csv.writerow(row) #Writes each row to the .csv file
    
unrandomized_cumulative_file= open('unrandomized_cumulative.csv', 'wb') #Opens a file
unrandomized_cumualtive_csv = csv.writer(unrandomized_cumulative_file) #Creates a csv object

unrandomized_cumualtive_csv.writerow(cumulative_header)

for row in all_cumulative_data:
    unrandomized_cumualtive_csv.writerow(row)
    
unrandomized_sharing_game_file.close()
unrandomized_cumulative_file.close()
original_data_file.close()
order_key_file.close()


