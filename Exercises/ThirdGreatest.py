def ThirdGreatest(strArr): 
	sorts = sorted(strArr, key=len)
   	sortedlen = [len(x) for x in sorts]
	for n in xrange(len(sortedlen)-1, -1, -1):
		if len(strArr[n]) == sortedlen[-3]:
			return strArr[n]
    
print ThirdGreatest(raw_input())  