def AdditivePersistence(num):
	count = 0
	def sumdigits(n):
		s = 0
		while n:
			s += n % 10
			n /= 10
		return s
	
	for ak in range(num):
		if len(str(num)) == 1:
			return count
		else: 
			num = sumdigits(num)
			count += 1
			continue
	return 0
	
print AdditivePersistence(raw_input())