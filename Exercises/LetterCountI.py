def LetterCountI(str): 
	wordlist = str.split()
	replist = []	
   	maxlist =[]
	def highestrep(x):
		reps = {}
		for c in x:
			try:
				reps[c] += 1
			except:
				reps[c] = 1
		return reps
	
	for word in wordlist:
		replist.append(highestrep(word))
    
	for n in replist:
		maxlist.append(max(n.values()))
    
	maxnumber = max(maxlist)
	return wordlist[maxlist.index(maxnumber)]
	
    
    
print LetterCountI(raw_input())  