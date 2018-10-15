def make_chocolate(small, big, goal):
    if (not ((small + big * 5) >= goal)):
        return -1
    while (True):
        if (goal >= 5 and big > 0):
            goal = goal - 5
            big = big - 1
        else:
            break
    if (goal <= small):
        return goal
    else:
        return -1
    return 0
