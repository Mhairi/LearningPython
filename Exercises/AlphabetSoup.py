def AlphabetSoup(str):
	temp = list(str)
	temp.sort()  
	for x in temp:
		print x

AlphabetSoup(raw_input())
