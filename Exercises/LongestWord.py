def LongestWord(sen): 
    temp = sen
    temp = "".join([c for c in temp if c not in ('(', ')', '?', ':', ';', ',', '.', '!', '/', '"', "'")])
    #for each character in temp, joins the character if c not in a list of characters
    words = temp.split()
    print max(words, key = len)
    return
    
LongestWord(raw_input())  
