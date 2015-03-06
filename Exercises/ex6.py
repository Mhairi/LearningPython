x = "There are %d types of people." % 10 # displays string
binary = "binary" # defines binary as "binary"
do_not = "don't" # defines do_not as "don't"
y = "Those who know %s and those who %s." %(binary, do_not) # combination of the two strings (place 1)

print x # prints x
print y # prints y

print "I said: %r." % x # prints x within the string - %r gives '' (place 2)
print "I also said: '%s'." % y # prints y within the string (place 3)

hilarious = False # defines hilarious as False
joke_evaluation = "Isn't that joke so funny?! %r" # does not have a %

print joke_evaluation % hilarious # prints joke_evaluation with % hilarious (place 4)

w = "This is the left side of..." # defines w as string
e = "a string with a right side." # defines e as string

print w + e # combines w and e
