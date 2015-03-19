def VowelCount(str): 
	vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
	vowels.count(str)
	temp = list(str)
	counter = 0
	for c in temp:
		if c in vowels:
			counter = counter + 1
	return counter
    
print VowelCount(raw_input())  
