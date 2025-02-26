class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        level_sum = dict()
        level_cnt = dict()
        visited = dict()
        stack = [(root,0)]
        while stack:
            top = stack[-1]
            if top in visited:
                level_sum[top[1]]  = level_sum.get(top[1], 0) + top[0].val
                level_cnt[top[1]]  = level_cnt.get(top[1], 0) + 1
                stack.pop(-1)
                continue
            if top[0].right is not None:
                stack.append( (top[0].right, top[1]+1) )
            if top[0].left is not None:
                stack.append( (top[0].left, top[1]+1) )
            visited[top] = True
        max_level = max(level_sum)
        ret = [level_sum[level]/level_cnt[level] for level in range(max_level+1)]
        return ret
