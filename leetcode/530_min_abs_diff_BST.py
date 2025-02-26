class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        root_child_val = root.left.val if root.left is not None else root.right.val
        min_diff = abs(root.val-root_child_val)
        visited = dict()
        prev = None
        stack = [root]
        while stack:
            top = stack.pop(-1)
            if top in visited:
                cur = top.val
                if prev is not None:
                    diff = abs(cur-prev)
                    if diff < min_diff:
                        min_diff = diff
                prev = cur
                continue
            if top.right is not None:
                stack.append(top.right)
            stack.append(top)
            if top.left is not None:
                stack.append(top.left)
            visited[top] = True
        return min_diff
        
        
        
