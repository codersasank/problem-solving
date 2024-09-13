class Solution:
    def mirror(self,root):
        stack = [root]
        visited = dict()
        while stack:
            top = stack[-1]
            if top in visited:
                top.left, top.right = top.right, top.left
                del visited[top]
                stack.pop(-1)
                continue
            if top.right is None and top.left is None:
                stack.pop(-1)
                continue
            if top.right is not None:
                stack.append(top.right)
            if top.left is not None:
                stack.append(top.left)
            visited[top] = True
