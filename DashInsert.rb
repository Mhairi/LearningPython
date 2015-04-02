def DashInsert(str)
  #split string into array
  str = str.to_s.split("")
  answer = "#{str[0]}"
  i = 1
  for i in i...str.length do
    if str[i].to_i.even? == false && str[i-1].to_i.even? == false then
      answer << "-#{str[i]}"
    else
      answer << "#{str[i]}"
    end
  end
return answer 
         
end