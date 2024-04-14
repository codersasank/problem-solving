class Solution:
    def countElements(self, a, b, n, query, q):
        a_s = sorted([(a[i],i) for i in range(n)]  )
        new_a_idx = dict()
        for i in range(n):
            new_a_idx[a_s[i][1]] = i
        b.sort()
        ret = list()
        idx = [-1]*n
        b_idx = 0
        for i in range(n):
            while b_idx<n:
                if a_s[i][0]>=b[b_idx]:
                    idx[i] = b_idx
                else:
                    break
                b_idx += 1
            if b_idx != 0:
                b_idx -= 1
        for q_idx in query:
            ret.append(idx[new_a_idx[q_idx]]+1 )
        return ret
            
