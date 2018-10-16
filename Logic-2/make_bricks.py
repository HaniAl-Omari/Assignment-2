def make_bricks(small, big, goal):
  if (not((small + big*5)>=goal)):
    return False
  while (True):
    if (goal >= 5 and big>0):
      goal = goal - 5
      big = big -1
    else:
      break
  if ( goal <= small):
    return True
  else:
    return False
  return True