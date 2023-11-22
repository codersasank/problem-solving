class Solution:
    # return true/false denoting whether the tree is Symmetric or not
    def isSymmetric(self, root):
        if root is None:
            return True
        stack1 , stack2 = list(), list()
        stack1.append(root) ; stack2.append(root)
        visited = dict()
        while stack1 and stack2:
            top1 = stack1[-1] ; top2 = stack2[-1]
            if top1 is None and top2 is None:
                stack1.pop(-1); stack2.pop(-1)
                continue
            elif top1 is None or top2 is None:
                return False
            else:
                pass
            if top1.data != top2.data:
                return False
            if visited.get(top1, False):
                stack1.pop(-1)
            if visited.get(top2, False):
                stack2.pop(-1)
            if visited.get(top1) and visited.get(top2):
                if top1 is top2:
                    visited.pop(top1)
                else:
                    visited.pop(top1) ; visited.pop(top2)
                continue
            stack1.append(top1.right)
            stack2.append(top2.left) 
            stack1.append(top1.left)
            stack2.append(top2.right)
            visited[top1]=True ; visited[top2]=True
        if not stack1 and not stack2:
            return True
        else:
            return False
