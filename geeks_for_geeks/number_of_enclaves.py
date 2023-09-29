from typing import List

class Solution:
    def numberOfEnclaves(self, grid: List[List[int]]) -> int:
        visited , cnt, stack = dict(), 0, list()
        n , m = len(grid), len(grid[0])
        one_count = sum([row.count(1) for row in grid])
        boundary = [ (i,j) for i in range(n) for j in range(m) if i==0 or i==n-1 or j==0 or j==m-1]
        
        for cell in boundary:
            if grid[cell[0]][cell[1]]==1 and not visited.get( (cell[0], cell[1]) , False):
                stack.append( (cell[0], cell[1]) )
            while stack:
                top = stack.pop(-1)
                if visited.get( (top[0], top[1]) , False):
                    continue
                if top[0]+1<n and grid[top[0]+1][top[1]]==1:
                    if not visited.get( (top[0]+1, top[1]) , False):
                        stack.append( (top[0]+1, top[1]) )
                if top[0]-1>=0 and grid[top[0]-1][top[1]]==1:
                    if not visited.get( (top[0]-1, top[1]) , False):
                        stack.append( (top[0]-1, top[1]) )
                if top[1]+1<m and grid[top[0]][top[1]+1]==1:
                    if not visited.get( (top[0], top[1]+1) , False):
                        stack.append( (top[0], top[1]+1) )
                if top[1]-1>=0 and grid[top[0]][top[1]-1]==1:
                    if not visited.get( (top[0], top[1]-1) , False):
                        stack.append( (top[0], top[1]-1) )
                visited[(top[0], top[1])] = True
                cnt += 1
                
        return one_count - cnt


