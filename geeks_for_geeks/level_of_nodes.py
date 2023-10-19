from collections import deque
class Solution:
    
    #Function to find the level of node X.
    def nodeLevel(self, V, adj, X):
        visited = dict()
        q = deque()
        q.append( (0,0) )
        while q:
            front = q.popleft()
            if front[0]==X:
                return front[1]
            for neighbour in adj[front[0]]:
                if neighbour==X:
                    return front[1]+1
                if not visited.get(neighbour, False):
                    q.append( (neighbour, front[1]+1) )
                    visited[neighbour] = True
        return -1
                
        
