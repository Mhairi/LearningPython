def CountingMinutesI(str)
  str = str.split("-")
  time1 = str[0]
  hour1 = time1.split(":")[0].to_i
  minutes1 = time1.split(":")[1]
  minutes1i = minutes1[0..1].to_i
  if minutes1[2..3] == "pm" then
    hour1 = hour1 + 12
  end   
  hour1m = hour1 *60
  t1 = hour1m + minutes1i
    
  time2 = str[1]
  hour2 = time2.split(":")[0].to_i
  minutes2 = time2.split(":")[1]
  minutes2i = minutes2[0..1].to_i
  if minutes2[2..3] == "pm" then
    hour2 = hour2 + 12
  end       
  hour2m = hour2 *60  
  t2 = hour2m + minutes2i
   
  if t2>t1 then
    return t2-t1
  else
    return t2+1440-t1  
  end
end
   