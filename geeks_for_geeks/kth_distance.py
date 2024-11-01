class Solution:
    def checkDuplicatesWithinK(self, arr, k):
        freq = dict()
        n = len(arr)
        for i in range(k+1):
            if arr[i] in freq:
                return True
            freq[arr[i]] = True
        for i in range(k+1,n):
            del freq[arr[i-k-1]]
            if arr[i] in freq:
                return True
            freq[arr[i]] = True
        return False
