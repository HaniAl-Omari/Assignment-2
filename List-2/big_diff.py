def big_diff(nums):
  mi=nums[0]
  ma=nums[0]
  for i in range(len(nums)):
    mi = min(mi,nums[i])
    ma = max(ma,nums[i])
  return ma-mi
