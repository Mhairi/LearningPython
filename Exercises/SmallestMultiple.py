def SmallestMultiple(n):
    testn = 1
    answer = 0
    while answer == False:
        for div in range (1,n+1):
            if testn % div == 0:
                pass
                if div == n:
                    answer = testn
            else:
                break
        testn += 1
    return answer 
    
print(SmallestMultiple(20))