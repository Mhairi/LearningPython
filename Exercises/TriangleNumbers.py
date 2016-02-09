import math

def nthtriangle(n):	#This function calculates the nth triangle number
	triangle = (n*(n+1))/2
	return triangle
	
def factors(n): #This function returns a list of factors for n
	factorlist = []
	for i in range(1,n):
		twopower = 2**i
		threepower = 3**i
		if n % twopower == 0:
			factorlist.append(twopower)
		elif n % threepower == 0:
			factorlist.append(threepower)
		else:
			pass
	return factorlist

print factors(28)
	
i = 1
	
#while len(factors(nthtriangle(i))) < 5:
#	i = i + 1
#	print len(factors(nthtriangle(i))) 
	
#print nthtriangle(i)