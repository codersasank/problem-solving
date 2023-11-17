class Solution:
    def __init__(self):
        self.head = None ; self.prev = None ; self.cur = None
    def inorder(self, root):
        if root is None:
            return
        if root.left is not None:
            self.inorder(root.left)
        root.left = self.prev
        if self.prev==None:
            self.head = root
        else:
            self.prev.right = root
        self.prev = root
        if root.right is not None:
            self.inorder(root.right)
    #Function to convert binary tree into circular doubly linked list.
    def bTreeToClist(self, root):
        self.inorder(root)
        cur = self.head
        while cur.right is not None:
            cur = cur.right
        self.head.left = cur ; cur.right = self.head
        return self.head
