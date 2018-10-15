def last2(str):
    if (len(str) < 2):
        return 0
    s = str[-2:]
    count = 0
    for i in range(len(str) - 2):
        part = str[i:i + 2]
        if part == s:
            count = count + 1

    return count