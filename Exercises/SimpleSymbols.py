def SimpleSymbols(str):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    temp = list(str)
  
    if temp[0] != "+" and temp[0] != "=":
        print "false"
        return
    
    for c in range(0, len(temp)):
        if temp[c] == "+" or temp[c] == "=":
            continue
        if temp[c] in alphabet and temp[c-1] == "+" and temp[c+1] == "+":
            continue
        else:
            print "false"
            return 
    print "true"
        
SimpleSymbols(raw_input())           
