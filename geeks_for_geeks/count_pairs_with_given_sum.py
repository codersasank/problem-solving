class Solution:
    def getPairsCount(self, arr, n, k):
        freq = dict() ; cnt = 0
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        if k%2==0:
            if k//2 in freq:
                cnt += (freq[k//2] * (freq[k//2]-1) ) //2
                freq[k//2] = 0
        for num in arr:
            if k-num in freq:
                cnt += freq.get(num, 0) * freq.get(k-num, 0)
                freq[num] = 0
        return cnt
