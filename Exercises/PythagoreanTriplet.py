#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#a2 + b2 = c2

#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

#How do we find the Pythagorean triplet that = 1000?
#Let's do it the inefficient way first: nested for loops.
# for c in range(400,600):
        # csq = c * c
        # for a in range(1,350):
            # for b in range(a,550):
                # if (a**2 + b**2 == csq) & (a + b + c == 1000):
                    # print a * b * c
                # else:
                    # pass
                    
# The above works, but how can we make it more efficient?
# We can use Euclid's formula, where for arbitrary m > n:  a = m^2 - n^2, b = 2mn, c = m^2 + n^2 
for n in range (1, 20):
    for m in range (n, 21):
        a = m**2 - n**2
        b = 2 * m * n
        c = m**2 + n **2
    #print a + b + c
    if a + b + c == 1000:
        print a, b, c
        
#Way faster. Yay!