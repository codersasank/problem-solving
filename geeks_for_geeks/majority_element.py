class Solution:
    def majorityElement(self, A, N):
        max_cnt = 0 ; ret = None
        freq = dict()
        for element in A:
            freq[element] = freq.get(element, 0) + 1
            if freq[element] > max_cnt:
                max_cnt = freq[element]
                ret = element
        if max_cnt > N/2:
            return ret
        return -1
