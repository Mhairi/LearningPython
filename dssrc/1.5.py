def compressstring(string):
    string = list(string)
    answer = []
    count = 1
    character = string[0]
    for x in range(0, len(string)):
        try:
            if string[x] == string[x+1]:
                count += 1
                character = string[x]
            else:
                answer.append(character)
                answer.append(count)
                character = string[x+1]
                count=1
        except IndexError:
                answer.append(character)
                answer.append(count)
        
    if len(answer) >= len(string):
        return string
    else:
        return answer
        
print(compressstring("hahasaaaaaaaaaaaah"))