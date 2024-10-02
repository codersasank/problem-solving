from collections import deque
class Solution:
    def catchThieves(self, arr, n, k):
        if n==1:
            return 0
        q = deque()
        i = 0
        cnt = 0
        while i<n:
            if not q:
                q.append(arr[i])
                i += 1
                continue
            if q[0] is None:
                q.popleft()
            elif q[0]=='P':
                if i<n and arr[i]!='T':
                    q.append(arr[i])
                    if len(q)>k:
                        q.popleft()
                        i += 1
                        continue
                    i += 1
                elif i<n and arr[i]=='T':
                    q.append(None)
                    q.popleft()
                    cnt += 1
                    i += 1
                if i>=n:
                    break
            else:
                if i<n and arr[i]!='P':
                    q.append(arr[i])
                    if len(q)>k:
                        q.popleft()
                        i += 1
                        continue
                    i += 1
                elif i<n and arr[i]=='P':
                    q.append(None)
                    q.popleft()
                    cnt += 1
                    i += 1
                if i>=n:
                    break
        return cnt
