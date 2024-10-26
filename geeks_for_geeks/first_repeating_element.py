class Solution:
    def firstRepeated(self,arr):
        n = len(arr)
        first = dict()
        last = dict()
        for i in range(n):
            num = arr[i]
            if num in first:
                last[num] = i
                continue
            first[num] = i
        idx = n
        for num in arr:
            if num in first and num in last:
                if first[num]<idx:
                    idx = first[num]
        return -1 if idx==n else idx+1
