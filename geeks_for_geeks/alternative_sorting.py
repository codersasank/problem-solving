class Solution:
    def alternateSort(self,arr):
        n = len(arr)
        arr.sort()
        pos = [0 for i in range(n)]
        ret = [0 for i in range(n)]
        for i in range(0,n,2):
            pos[i] = n-1-(i//2)
        for i in range(1,n,2):
            pos[i] = (i-1)//2
        for i in range(n):
            ret[i] = arr[pos[i]]
        return ret
