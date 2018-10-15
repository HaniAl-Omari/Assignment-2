def string_bits(str):
  s = "";
  i=0
  while(True):
    if(i>=len(str)):
      break
    s = s + str[i]
    i = i +2
  return s
