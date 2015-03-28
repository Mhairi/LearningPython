def ArithGeo(arr):
	end = len(arr)-1
	div = arr[1]/float(arr[0])
	diff = arr[1] - arr[0]
    
	if all(arr[i]/float(arr[i-1]) == div for i in xrange(1, len(arr))) == True:
		print "Geometric"
	elif all(arr[i] - arr[i-1] == diff for i in xrange(1, len(arr))) == True:
		print "Arithmetic"
	else:
		print "-1"
    
ArithGeo(raw_input())