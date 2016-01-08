#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#a2 + b2 = c2

#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

#How do we find the Pythagorean triplet that = 1000?
#Let's do it the inefficient way first: nested for loops.
for c in range(400,600):
        csq = c * c
        for a in range(1,350):
            for b in range(a,550):
                if (a**2 + b**2 == csq) & (a + b + c == 1000):
                    print a * b * c
                else:
                    pass
                    
# The above works, but how can we make it more efficient?