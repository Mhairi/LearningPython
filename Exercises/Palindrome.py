def Palindrome(str):
	temp = list(str)
	temp = "".join([c for c in temp if c not in (" ")])
	temp2 = temp[::-1]
	if temp == temp2:
		print "true"
	elif temp != temp2:
		print "false"

Palindrome(raw_input())