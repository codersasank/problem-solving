def remdup(l):
    present = dict()
    for num in l:
        present[num] = present.get(num,0) + 1
    ret = list()
    for num in l:
        if present[num]==1:
            ret.append(num)
        else:
            present[num] -= 1
    return ret
