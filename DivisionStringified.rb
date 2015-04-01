def DivisionStringified(num1,num2)
  num = num1/num2
  numstr= num.to_s
  numstr = numstr.split("")
  finstr=[]
  i = numstr.length-1
  count = 0
  while i > -1
    if (count % 3 == 0 && count != 0) then
      finstr.unshift(",")
    end
      finstr.unshift("#{numstr[i]}")
    i -= 1     
    count +=1
  end
  return finstr.join("")
end
    
print DivisionStringified(123456789   ,10000 )  
