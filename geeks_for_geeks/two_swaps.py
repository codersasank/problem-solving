class Solution:
    def checkSorted(self, arr):
        swaps = 0
        i = 0
        n = len(arr)
        while i<n:
            if arr[i]==i+1:
                i += 1
                continue
            if swaps>=2:
                return False
            idx = arr[i]-1
            tmp = arr[i]
            arr[i] = arr[idx]
            arr[idx] = tmp
            swaps += 1
        if swaps==2 or swaps==0:
            return True
        else:
            return False
