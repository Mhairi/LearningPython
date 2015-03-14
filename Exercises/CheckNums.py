def CheckNums(num1, num2):
  	num1a = int(num1)
  	num2a = int (num2)
	if num1a == num2a:
		print "-1"
	elif num2a > num1a:
		print "true"
	else:
		print "false"
	return
			
CheckNums(raw_input())  

