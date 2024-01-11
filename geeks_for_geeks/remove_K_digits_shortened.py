class Solution:
    def removeKdigits(self, S, K):
        n = len(S)
        if K==n-1:
            return min(S)
        if K==n:
            return 0
        ret = list() ; popped = 0
        idx = 1 ; ret.append(S[0])
        while idx<n:
            while ret and popped<K and ((ret[-1]) > (S[idx])):
                ret.pop(-1); popped += 1
            ret.append(S[idx]) ; idx += 1
        ret += S[idx:]
        ret = ret[:n-K]
        return int(''.join(ret))
