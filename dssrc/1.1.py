def uniquestring(string):
    splitstring = list(string)
    dict = {}
    
    for letter in splitstring:
        try:
            dict[letter] += 1
        except KeyError:
            dict[letter] = 1
            
    print(dict)
    
    for key in dict:
        if dict[key] > 1:
            return True
        else:
            pass
        
    return False