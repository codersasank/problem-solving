class Solution:
    def floor(self, root, x):
        temp = root
        prev = None
        while temp is not None:
            if temp.data < x:
                prev = temp
                temp = temp.right
                continue
            elif temp.data > x:
                temp = temp.left
                continue
            else:
                return x
        if prev is None or prev.data>x:
            return -1
        else:
            return prev.data
