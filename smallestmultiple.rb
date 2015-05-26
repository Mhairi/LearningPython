#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
def divvy(i, num) 
  p = 1
  for p in p..num do
    if i % p !=0
      return false
    end
  end
  return true
end

def smallestmultiple(num)
  i = 1 #this is the value we are testing
  poop = false
  while poop == false #go to helper function and divide i by every number from 1 to num
    poop = divvy(i, num)  #divvy returns true if the number is divisible by all digist from 1 to num  
    i += 1
    #print "#{i}, #{num}, #{poop = divvy(i, num)}"
  end
  return i-1
end

print smallestmultiple(20)