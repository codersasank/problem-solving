class Solution:
    def nthRowOfPascalTriangle(self,n):
        cur = None ; nxt = [1]
        divisor = 10**9 + 7
        for i in range(1,n+1):
            cur = nxt
            nxt = [0]*(i+1)
            for j in range(i+1):
                nxt[j] = ((cur[j-1] if j>0 else 0)%divisor + (cur[j] if j<i else 0)%divisor)%divisor
        return cur

