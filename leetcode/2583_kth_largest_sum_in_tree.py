import heapq
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        level_sum = [0]
        stack = [(root,0)]
        visited = dict()
        while stack:
            top = stack[-1]
            if top in visited:
                stack.pop(-1)
                val, level = top[0].val, top[1]
                level_sum[level] += val
                continue
            visited[top] = True
            if top[0].right is not None:
                stack.append( (top[0].right, top[1]+1) )
                if top[1]+2>len(level_sum):
                    for i in range(top[1]+2-len(level_sum)):
                        level_sum.append(0)
            if top[0].left is not None:
                stack.append( (top[0].left, top[1]+1) )
                if top[1]+2>len(level_sum):
                    for i in range(top[1]+2-len(level_sum)):
                        level_sum.append(0)
        if len(level_sum)<k:
            return -1
        k_largest = heapq.nlargest(k, level_sum)
        return k_largest[-1]
