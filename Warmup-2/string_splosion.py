def string_splosion(str):
  s = ""
  for i in range(len(str)):
    for j in range(i+1):
      s = s + str[j]
  return s