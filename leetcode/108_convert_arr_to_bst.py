class Solution:
    def form_tree(self, nums, left, right):
        if left > right:
            return None
        elif left == right:
            return TreeNode(nums[left])
        else:
            mid = (left+right)//2
            root = TreeNode(nums[mid])
            root.left = self.form_tree(nums, left, mid-1)
            root.right = self.form_tree(nums, mid+1, right)
            return root
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.form_tree(nums, 0, len(nums)-1)

        
