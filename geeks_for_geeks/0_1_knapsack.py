class Solution:
    def knapSack(self,W, wt, val, n):
        sack_val = [ [0 for j in range(W+1)] for i in range(n+1) ]
        for i in range(n+1):
            sack_val[i][0] = 0
        for j in range(W+1):
            sack_val[0][j] = 0
        for i in range(1,n+1):
            for j in range(1,W+1):
                if wt[i-1] > j:
                    sack_val[i][j] = sack_val[i-1][j]
                else:
                    sack_val[i][j] = max ( sack_val[i-1][j], sack_val[i-1][j-wt[i-1]] + val[i-1]  )
        
        return sack_val[n][W]
