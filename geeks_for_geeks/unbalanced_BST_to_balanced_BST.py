class Solution:
    def balanced(self, lst, start, end):
        if start>end:
            return None
        if start==end:
            middle = lst[start]
            middle.left = middle.right = None
            return middle
        middle_idx = (start+end)//2
        middle = lst[ middle_idx ]
        middle.left = self.balanced(lst, start, middle_idx-1)
        middle.right = self.balanced(lst, middle_idx+1, end)
        return middle
    def inorder(self, root, lst):
        if root is None:
            return
        self.inorder(root.left, lst)
        lst.append(root)
        self.inorder(root.right, lst)
    def buildBalancedTree(self,root):
        lst = list()
        self.inorder(root,lst)
        n = len(lst)
        new_root = self.balanced(lst, 0, n-1)
        return new_root
