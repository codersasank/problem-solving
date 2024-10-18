class Solution:
    def bst(self, low, high, nums):
        if low>high:
            return None
        mid = (low+high)//2
        root = Node(nums[mid])
        root.left = self.bst(low, mid-1, nums)
        root.right = self.bst(mid+1, high, nums)
        return root
        
    def sortedArrayToBST(self, nums):
        n = len(nums)
        return self.bst(0, n-1, nums)
