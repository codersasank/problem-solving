class Solution:
    def removeKdigits(self, S, K):
        n = len(S)
        if K==n-1:
            return min(S)
        if K==n:
            return 0
        ret = list() ; popped = 0 ; cnt = 1
        idx = 1 ; ret.append(S[0])
        while popped < K and idx<n:
            if int(ret[-1]) > int(S[idx]):
                while ret and idx<n and popped<K and (int(ret[-1]) >= int(S[idx])):
                    ret.pop(-1); popped += 1
                    cnt -= 1
                ret.append(S[idx]) ; idx += 1
                cnt += 1
            else:
                ret.append(S[idx])
                idx += 1 ; cnt += 1
        while cnt<n-K and idx<n:
            ret.append(S[idx])
            idx += 1
        ret = ret[:n-K]
        return ''.join(ret)
