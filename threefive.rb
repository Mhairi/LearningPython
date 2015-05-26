#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

def threefive
  #don't want to double count multiples of both 3 and five
  i = 1
  n = 0
  #do we want to push to an array, or just add to a sum (n= n+ i)?
  while i < 1000
    if i % 3 == 0 && i % 5 == 0 then
      n = n + i
    elsif i % 3 == 0 && i % 5 != 0 then
      n = n + i
    elsif i % 5 == 0 && i % 3 != 0 then
      n = n + i
    end #end of if
      i += 1
    end #end of while
      return n
    end #end of def
      
      puts threefive()