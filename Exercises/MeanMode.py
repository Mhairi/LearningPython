def MeanMode(arr): 
	Mean = float(sum(arr))/len(arr)
    Mode = max(((item, arr.count(item)) for item in set(arr)), key = lambda a: a[1])[0]
	#from inside to out: for item in the set, return the item, and it's count. then, look for the max count (a[1]), and return the item (a[0])
    if Mean == Mode:
    	return 1
    if Mean != Mode:
      	return 0
	
print MeanMode(raw_input())  
















  