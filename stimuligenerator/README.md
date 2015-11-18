####stimuligenerator.py####
Contains all the functions that produce stimuli for each of the options (favoring self, favoring partner, favoring group over self, favoring group over partner). For the latter two, the group-favoring option can be both partner or self favoring (or equal) - the only criteria is that the group sum for that option is larger than for the other option.
This can be modified produce other values (e.g., multiples of 5).

####testing.py####
Runs a bunch of tests to make sure that those functions produce the right stimuli (e.g., that the favoring self condition assigns more to the self than to the other person).

####scripttogeneratestimuli.py####
Generates as many stimuli as we want, and writes it to a .csv file.
