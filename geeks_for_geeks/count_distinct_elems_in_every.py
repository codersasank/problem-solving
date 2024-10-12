class Solution:
    def countDistinct(self, A, N, K):
        freq = dict()
        distinct_cnt = 0
        ret = list()
        for i in range(K):
            num = A[i]
            if num in freq:
                freq[num] += 1
                continue
            else:
                freq[num] = 1
                distinct_cnt += 1
        ret.append(distinct_cnt)
        for i in range(K, N):
            prev = A[i-K]
            if freq[prev]==1:
                distinct_cnt -= 1
            freq[prev] -= 1
            cur = A[i]
            if cur not in freq or freq[cur]==0:
                distinct_cnt += 1
            freq[cur] = freq.get(cur, 0) + 1
            ret.append(distinct_cnt)
        return ret            
