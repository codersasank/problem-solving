class Solution:
    def bsearch(self, A, left, right, X):
        if left>right:
            return -1
        if left==right:
            if A[left]==X:
                return left
            elif A[left]<X:
                return left+1
            else:
                return -1
        mid = (left+right)//2
        if A[mid]==X:
            return mid
        elif A[mid]<X:
            if (mid==len(A)-1) or (A[mid+1]>X):
                return mid+1
            else:
                return self.bsearch(A, mid+1, right, X)
        else:
            return self.bsearch(A, left, mid-1, X)
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums[0]>=target:
            return 0
        return self.bsearch(nums, 0, len(nums)-1, target)
