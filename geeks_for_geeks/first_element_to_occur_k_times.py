class Solution:
    def firstElementKTime(self, n, k, a):
        max_cnt = 0 ; elem = None
        freq = dict()
        for num in a:
            freq[num] = freq.get(num, 0) + 1
            if freq[num] > max_cnt:
                elem = num ; max_cnt = freq[num]
            if max_cnt==k:
                return elem
        if max_cnt < k:
            return -1
