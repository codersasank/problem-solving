class Solution:
    def sumMatrix(self, n, q):
        ret = 0
        if q>2*n:
            return 0
        else:
            if q%2==0:
                ret = (q//2)*2 - 1
            else:
                ret = (q//2)*2
            if q<=n:
                return ret
            else:
                return ret - (q-1-n)*2
