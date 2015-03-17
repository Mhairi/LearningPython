def ABCheck(str):
	temp = list(str)
	for c in range(0, len(temp)):
		try:
			if temp[c] == "a" and temp[c + 4] == "b":
				return "true"
            if temp[c] == "b" and temp[c + 4] == "a":
              	return "true"
		except IndexError:
			continue
	return "false"

print ABCheck(raw_input())