def combo_string(a, b):
  m= min(len(a),len(b))
  if(m==len(a)):
    return a+b+a
  return b+a+b
