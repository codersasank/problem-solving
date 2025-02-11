def remdup(l):
    present = dict()
    for num in l:
        present[num] = present.get(num,0) + 1
    l.reverse()
    idx = len(l) - 1
    while idx >= 0:
        num = l[idx]
        if present[num] > 1:
            l.pop(-1)
            present[num] -= 1
        idx -= 1
    l.reverse()
