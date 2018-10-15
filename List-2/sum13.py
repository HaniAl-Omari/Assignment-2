def sum13(nums):
  if (len(nums) == 0):
    return 0;
  sum = 0
  for i in range(len(nums)):
    if ( nums[i] != 13 and (i==0 or nums[i-1] != 13)):
      sum = sum + nums[i]
  return sum
