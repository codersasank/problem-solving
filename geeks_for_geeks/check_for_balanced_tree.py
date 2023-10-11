class Solution:
    def __init__(self):
        self.balanced = True
    def tree_height(self,root):
        if root is None:
            return -1
        if not self.balanced:
            return 0
        left_height = self.tree_height(root.left)
        right_height = self.tree_height(root.right)
        if not abs(left_height-right_height)<=1:
            self.balanced = False
            return 0
        return max([left_height, right_height])+1
            
    def isBalanced(self,root):
        self.tree_height(root)
        return self.balanced

