class Solution:
    def inorder(self, root, lst):
        if root.left is not None:
            self.inorder(root.left, lst)
        lst.append(root.data)
        if root.right is not None:
            self.inorder(root.right, lst)
    def countPairs(self, root1, root2, x):
        list1, list2 = list(), list()
        self.inorder(root1, list1)
        self.inorder(root2, list2)
        dict2 = {num:True for num in list2 }
        cnt = 0
        for num in list1:
            if x-num in dict2:
                cnt += 1
        return cnt
        
