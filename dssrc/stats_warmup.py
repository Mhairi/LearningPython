def mean(array):
    counter = 0
    for i in range(0,len(array)):
        counter += array[i]
        
    return float(counter)/float(len(array))
     
def meanlist(array):
    counter = sum(array)
    return float(counter)/(len(array))

def factorial(n):
    answer = 1
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        for i in range(1,n+1):
            answer = answer * i
    return answer

def factorialrecursion(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorialrecursion(n-1)
    
def twomultiplier(array): #return an array where all the numbers are multiplied by 2
    return [x*2 for x in array]

    
def threefilter(array): #filters multiples of three
    def threemult(x):
        return x%3 == 0
    return filter(threemult, array) #function returns true if multiple of 3
    #return filter(lambda x: x % 3== 0, array) #in one line using lambdas
    
    
def twoadder(array):
    return map(lambda x: x+2, array)
    
def factorialreduce(n):
    if n == 0:
        return 1
    else:
        return reduce(lambda x,y: x*y, range(1,n+1))
    
print factorialreduce(0)
            