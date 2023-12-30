class Solution:
    def minPartition(self, N):
        denom = [2000,500,200,100,50,20,10,5,2,1]
        idx = 0 ; cnt = 0 ; temp = N
        ret = list()
        while temp > 0 and idx<=9:
            if denom[idx] <= temp:
                ret.append(denom[idx])
                cnt += 1
                temp -= denom[idx]
            else:
                idx += 1
        return ret
        
