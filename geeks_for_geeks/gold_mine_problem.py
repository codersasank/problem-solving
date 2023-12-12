class Solution:
    def maxGold(self, n, m, M):
        max_gold = [[ 0 for j in range(m) ] for i in range(n)]
        for i in range(n):
            max_gold[i][0] = M[i][0]
        for j in range(1,m):
            for i in range(n):
                max_gold[i][j] = max ( max_gold[i-1][j-1] if i>0 else 0, max_gold[i+1][j-1] if i+1<n else 0, max_gold[i][j-1]  )
                max_gold[i][j] += M[i][j]
        max_collected = max_gold[0][m-1]
        for i in range(n):
            if max_gold[i][m-1]>max_collected:
                max_collected = max_gold[i][m-1]
        return max_collected
