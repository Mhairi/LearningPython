def stringperm(string1,string2):
    s1 = list(string1)
    s2 = list(string2)
    s1 = sorted(s1)
    s2 = sorted(s2)
    if s1 == s2:
        return True
    else:
        return False
        
print(stringperm("hello", "olleh"))