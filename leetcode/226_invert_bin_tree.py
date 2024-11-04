class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        stack = [root]
        visited = dict()
        while stack:
            top = stack[-1]
            if top in visited:
                stack.pop(-1)
                top.left, top.right = top.right, top.left
                del visited[top]
                continue
            if top.right is not None:
                stack.append(top.right)
            if top.left is not None:
                stack.append(top.left)
            visited[top] = True
        return root
