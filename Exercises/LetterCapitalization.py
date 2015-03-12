def LetterCapitalization(str):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 
                'x', 'y', 'z']
    
    allcaps = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 
                'X', 'Y', 'Z']
    
    sentence = ""
    
    temp = list(str)

    if temp[0] in alphabet:
        temp[0] = temp[0].replace(temp[0], allcaps[alphabet.index(temp[0])])
    
    for c in range(0, len(temp)):
        if temp[c-1] != " ":
            sentence = sentence + temp[c]
        if temp[c] == " " and temp[c+1] in alphabet:
            char = temp[c+1].replace(temp[c+1], allcaps[alphabet.index(temp[c+1])])
            sentence = sentence + char
            
    print sentence
    return
    
LetterCapitalization(raw_input())