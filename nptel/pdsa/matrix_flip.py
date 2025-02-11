def matrixflip(m,d):
    ret = list()
    if d=='h':
        for row in m:
            ret.append(row[::-1])
    elif d=='v':
        for idx in range(len(m)-1, -1, -1):
            ret.append(m[idx][:])
    return ret
        
