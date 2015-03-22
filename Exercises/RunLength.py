def RunLength(abc):
	temp = list(abc)
	counter = 1
	newstr = []
	for c in range(0, len(temp)):
		try:
			if temp[c] == temp[c+1]:
				counter += 1
			else:
				newstr.append(counter)
				newstr.append(temp[c])
				counter = 1
		except IndexError:
				newstr.append(counter)
				newstr.append(temp[c])
				continue
	print "".join(map(str, newstr))

RunLength(raw_input())