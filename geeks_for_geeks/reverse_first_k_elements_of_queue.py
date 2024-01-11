from collections import deque 

class Solution:
    def modifyQueue(self, q, k):
        n = len(q)
        q = deque(q)
        stack = list() ; cnt = 0
        while cnt<k:
            stack.append(q.popleft())
            cnt += 1
        while cnt>0:
            q.append(stack.pop(-1))
            cnt -= 1
        while cnt<n-k:
            q.append(q.popleft())
            cnt += 1
        return q
        
