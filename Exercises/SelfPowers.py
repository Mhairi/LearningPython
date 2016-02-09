#Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

#Inefficiently:
tally = 0
for i in range(1, 1001):
    tally = tally + i**i

print tally

#It works!