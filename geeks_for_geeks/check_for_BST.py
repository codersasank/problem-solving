class Solution:
    def checkBST(self, lwr_lmt, upr_lmt, root):
        if root is None:
            return True
        if root.left is not None and root.left.data >= root.data:
            return False
        if root.right is not None and root.right.data <= root.data:
            return False
        if not self.checkBST(lwr_lmt, root.data, root.left):
            return False
        if not self.checkBST(root.data, upr_lmt, root.right):
            return False
            
        if lwr_lmt is not None and root.data<=lwr_lmt:
            return False
        if upr_lmt is not None and root.data>=upr_lmt:
            return False
            
        return True
        
    def isBST(self, root):
        return self.checkBST(None, None, root)
