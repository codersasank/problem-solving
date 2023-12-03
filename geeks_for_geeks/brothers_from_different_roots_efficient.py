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
        cnt = 0
        n1, n2 = len(list1), len(list2)
        idx1 , idx2 = 0, n2-1
        while idx1<n1 and idx2>=0:
            if list1[idx1]+list2[idx2]<x:
                idx1 += 1
                continue
            elif list1[idx1]+list2[idx2]==x:
                cnt += 1 ; idx1 += 1 ; idx2 -=1
                continue
            else:
                idx2 -= 1
        return cnt
