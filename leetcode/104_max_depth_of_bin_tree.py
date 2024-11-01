class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        stack = [(root,1)]
        visited = dict()
        max_depth = 1
        while stack:
            top, depth = stack[-1][0], stack[-1][1]
            if depth > max_depth:
                max_depth = depth
            if top in visited:
                del visited[top]
                stack.pop(-1)
                continue
            if top.right is not None:
                stack.append( (top.right, depth+1) )
            if top.left is not None:
                stack.append( (top.left, depth+1) )
            visited[top] = True
        return max_depth
