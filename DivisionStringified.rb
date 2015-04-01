def DivisionStringified(num1,num2)
  num = num1/num2
  numstr= num.to_s
  i = 0
  finstr = ""
  for i in i...numstr.length do
    if i == 2 && numstr.length > 3 then
      finstr << ",#{numstr[i]}"
    else
    finstr << numstr[i]
    end
  end
  return finstr
end
    
print DivisionStringified(123456789  ,10000  )  
