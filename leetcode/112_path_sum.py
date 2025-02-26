class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        visited = dict()
        stack = [root]
        path_sum = 0
        while stack:
            top = stack[-1]
            if top in visited:
                path_sum -= top.val
                stack.pop(-1)
                continue
            path_sum += top.val
            if (top.left is None) and (top.right is None) and (path_sum == targetSum):
                return True
            if top.right is not None:
                stack.append(top.right)
            if top.left is not None:
                stack.append(top.left)
            visited[top] = True
        return False
        
