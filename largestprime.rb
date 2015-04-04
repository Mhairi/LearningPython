def largestprime
  i = 2 #iterate from 2 to whatever number
  largest = 0 #used to store the largest value so far
  while i < 600851475143
    if i % 2 != 0 && i % 3 != 0 && i % 4 != 0 && i % 5 != 0 then
      if 600851475143 % i == 0 then
        test = 600851475143/i
        if test % 2 != 0 && test % 3 != 0 && test % 4 != 0 && test % 5 != 0 then
        largest = test
        puts largest
        end
        end
      
      end
        i += 1
    end
    puts "done!"
  end
  
  largestprime()