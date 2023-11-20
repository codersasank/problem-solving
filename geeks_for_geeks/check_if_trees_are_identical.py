class Solution:
    #Function to check if two trees are identical.
    def isIdentical(self,root1, root2):
        stack1 , stack2 = list(), list()
        stack1.append(root1) ; stack2.append(root2)
        visited = dict()
        while stack1 and stack2:
            top1 = stack1[-1] ; top2 = stack2[-1]
            if top1.data != top2.data:
                return False
            if visited.get(top1, False):
                stack1.pop(-1)
            if visited.get(top2, False):
                stack2.pop(-1)
            if visited.get(top1) and visited.get(top2):
                visited.pop(top1) ; visited.pop(top2)
                continue
            if top1.right is not None:
                stack1.append(top1.right)
            if top2.right is not None:
                stack2.append(top2.right)                
            if top1.left is not None:
                stack1.append(top1.left)
            if top2.left is not None:
                stack2.append(top2.left)
            visited[top1]=True ; visited[top2]=True
        if not stack1 and not stack2:
            return True
        else:
