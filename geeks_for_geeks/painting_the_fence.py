class Solution:
    def countWays(self,n,k):
        if n==1:
            return k
        divisor = 10**9 + 7
        same_as_earlier = [0 for i in range(n) ]
        unlike_earlier = [0 for i in range(n) ]
        same_as_earlier[0] = 0 ; unlike_earlier[0] = k%divisor
        for i in range(1,n):
            same_as_earlier[i] = unlike_earlier[i-1]
            unlike_earlier[i] = ( ((k-1)%divisor)*( (same_as_earlier[i-1] + unlike_earlier[i-1])%divisor) )%divisor
        result = (same_as_earlier[n-1]%divisor + unlike_earlier[n-1]%divisor)%divisor
        return result

