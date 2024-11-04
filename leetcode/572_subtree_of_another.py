class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p is None and q is not None) or (p is not None and q is None):
            return False
        if (p is None and q is None):
            return True
        if (p.val == q.val) and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
            return True
        else:
            return False
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = [root]
        visited = dict()
        while stack:
            top = stack[-1]
            if top not in visited and self.isSameTree(subRoot, top):
                return True
            if top in visited:
                stack.pop(-1)
                del visited[top]
                continue
            if top.right is not None:
                stack.append(top.right)
            if top.left is not None:
                stack.append(top.left)
            visited[top] = True
        return False
