def SimpleAdding(num): 
    number = int(num)
    counter = 1
    x=0
    for n in range(0,number):
        x = x + counter
        counter += 1
    return x

print SimpleAdding(raw_input())  