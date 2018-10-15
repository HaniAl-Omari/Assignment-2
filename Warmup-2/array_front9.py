def array_front9(nums):
    count = 0
    if (len(nums) < 4):
        r = len(nums)
    else:
        r = 4
    for i in range(r):
        if (nums[i] == 9):
            return True

    return False
