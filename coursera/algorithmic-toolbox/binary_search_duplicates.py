def bsearch(arr, left, right, x):
    mid = (left+right)//2
    if left>right or left<0:
        return -1
    if arr[mid]==x:
        return mid
    elif arr[mid]<x:
        return bsearch(arr, mid+1, right, x)
    else:
        return bsearch(arr, left, mid-1, x)
    
def binary_search(keys, query):
    n = len(keys)
    idx = bsearch(keys, 0, n-1, query)
    if idx==-1:
        return -1
    match = temp_idx = idx
    while temp_idx!=-1:
        temp_idx = bsearch(keys, 0, temp_idx-1, query)
        if temp_idx!=-1:
            match = temp_idx
    if match!=idx:
        return match
    else:
        return idx
