def listtype(l):
  return(type(l) == type([]))

def flatten(l):
    ret = list()
    for item in l:
        if not listtype(item):
            ret.append(item)
        else:
            ret.extend(flatten(item))
    return ret
