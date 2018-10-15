def caught_speeding(speed, is_birthday):
  if(speed<=60 or (is_birthday and speed<=65 )):
    return 0
  if (60<speed and speed<=80 or (is_birthday and 60<speed and speed<=85 )):
    return 1
  if (80 < speed or (is_birthday and 85 < speed )):
    return 2
