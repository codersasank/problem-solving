class Solution:
    def bsearch(self, left, right, X):
        if left>right:
            return -1
        if left==right:
            if left**2==X:
                return left
            elif left**2<X:
                return left
            else:
                return -1
        mid = (left+right)//2
        if mid**2==X:
            return mid
        elif mid**2<X:
            if (mid==X-1) or ((mid+1)**2>X):
                return mid
            else:
                return self.bsearch(mid+1, right, X)
        else:
            return self.bsearch(left, mid-1, X)
    def floorSqrt(self, n):
        if n==1:
            return 1
        return self.bsearch(0, n-1, n)
