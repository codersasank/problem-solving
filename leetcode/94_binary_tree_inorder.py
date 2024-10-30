class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ret = list()
        visited = dict()
        if root is None:
            return []
        stack = [root]
        while stack:
            top = stack.pop(-1)
            if top in visited:
                ret.append(top.val)
                del visited[top]
                continue
            if top.right is not None:
                stack.append(top.right)
            stack.append(top)
            if top.left is not None:
                stack.append(top.left)
            visited[top] = True
        return ret
