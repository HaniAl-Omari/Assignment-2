def string_match(a, b):
  counter = 0
  m = min(len(a),len(b))
  for i in range(0,m-1,1):
      if(a[i:i+2]==b[i:i+2]):
        counter = counter + 1 
  return counter
