def rotatelist(l,k):
    if k <= 0:
        return l
    rot = k%len(l)
    new_lst = l[rot:len(l)+1] + l[0:rot]
    return new_lst
