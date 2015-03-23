def SecondGreatLow(arr): 
  	temp2 = set(arr)
	temp = sorted(temp2)
    
	if len(arr) == 2:
		temp3 = sorted(arr)
		return "%s %s" % (arr[1], arr[0])
	return "%s %s" %(temp[1], temp[len(temp)-2])

print SecondGreatLow(raw_input())  










  