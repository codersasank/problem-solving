def splitsum(l):
    pos = neg = 0
    for num in l:
        if num > 0:
            pos += num**2
        else:
            neg += num**3
    return [pos, neg]
