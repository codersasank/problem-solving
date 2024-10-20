class Solution:
    def maximizeSum(self, a, n, k):
        total = sum(a)
        ops = k
        a.sort()
        i = 0
        while ops>0 and i<n and a[i]<0:
            total -= 2*a[i]
            ops -= 1
            i += 1
        min_val = min(a, key=lambda x:abs(x))
        if ops%2==0:
            return total
        total -= 2*abs(min_val)
        return total
