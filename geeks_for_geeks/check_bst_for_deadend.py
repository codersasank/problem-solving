class Solution:
    def isDeadEnd(self, root):
        upper = 10002 ; lower = 0 ; stack = list()
        limits = dict() ; limits[root] = (lower, upper)
        stack.append(root) ; visited = dict()
        while stack:
            top = stack[-1]
            if visited.get(top,False):
                stack.pop(-1)
                if limits[top][0]==top.data-1 and limits[top][1]==top.data+1:
                    return True
                continue
            if top.right is not None:
                stack.append(top.right)
                limits[top.right] = ( top.data, limits[top][1] )
            if top.left is not None:
                stack.append(top.left)
                limits[top.left] = ( limits[top][0], top.data )
            visited[top] = True
        return False
