def LetterChanges(str): 
	alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 
                'x', 'y', 'z', 'a']
    
	vowel = ['a', 'e', 'i', 'o', 'u']
    
	vowelcap = ['A', 'E', 'I', 'O', 'U']
    
	temp = str
	abc = ""
	de = ""
	for n in range(0, len(temp)):
		if temp[n] in alphabet:
			#alphabet.index(temp[n])
			char = temp[n].replace(temp[n],alphabet[alphabet.index(temp[n]) + 1])
			abc = abc + char
		else:
			abc = abc + temp[n]
	
	for n in range(0, len(abc)):
		if abc[n] in vowel:
			#vowel.index(abc[n])
			char = abc[n].replace(abc[n],vowelcap[vowel.index(abc[n])])
			de = de + char
		else:
			de = de + abc[n]
	print de
	return 
 
LetterChanges(raw_input())  