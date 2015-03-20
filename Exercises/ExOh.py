def ExOh(str):
	temp = list(str)
	xcount = 0
	ocount = 0
	for c in temp:
		if c == "x":
			xcount += 1
		if c == "o":
			ocount += 1
	
	if xcount == ocount:
		print "true"
	elif xcount != ocount:
		print "false"

ExOh(raw_input())