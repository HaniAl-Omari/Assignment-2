def rotate_left3(nums):
  num = nums[0]
  nums[0] = nums[1]
  nums[1] = nums[2]
  nums[2] = num;
  return nums
