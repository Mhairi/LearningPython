import pandas as pd
import os
rootdir = 'C:/Users/Bryan/Desktop/MT_corrected'

def self_chips(line):
    pid = ""
    answer = ""
    for i, char in enumerate(line):
        if i <= 6:
            pid = str(pid) + str(char)
        if i > 63 and i < 67:
            answer = answer + char
    return [pid, answer]

def all_participant_colors(rootdir):    
    participant_colors = []
    
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            file_name = open(rootdir + "/" + file)
        
            for i, line in enumerate(file_name):
                try:
                    if i > 4 and i < 75 and line[23] == 'Y':  
                        participant_colors.append(self_chips(line))
                except IndexError:
                    pass
            file_name.close()
    return participant_colors


hopefully_this_works = all_participant_colors(rootdir)
hopefully_this_works = pd.DataFrame(hopefully_this_works)
hopefully_this_works.to_csv("answer.csv", index = False, header = False)

