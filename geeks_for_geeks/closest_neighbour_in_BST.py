class Solution:
    def findMaxForN(self, root, n):
        cur = root
        if cur.key == n:
            return n
        elif cur.key > n:
            if cur.left is None:
                return -1
            else:
                return self.findMaxForN(cur.left, n)
        else:
            if cur.right is None:
                return cur.key
            else:
                return max(self.findMaxForN(cur.right, n), cur.key)
            
