class Solution:
    def bsearch(self, A, left, right, X):
        if left>right:
            return -1
        if left==right:
            if A[left]==X:
                return left
            elif A[left]<X:
                return left
            else:
                return -1
        mid = (left+right)//2
        if A[mid]==X:
            return mid
        elif A[mid]<X:
            if (mid==len(A)-1) or (A[mid+1]>X):
                return mid
            else:
                return self.bsearch(A, mid+1, right, X)
        else:
            return self.bsearch(A, left, mid-1, X)
    def findFloor(self,A,N,X):
        return self.bsearch(A, 0, N-1, X)
