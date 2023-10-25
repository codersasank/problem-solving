class Solution:
    def knapSack(self, N, W, val, wt):
        max_profit = [0]*(W+1)
        val_wt = [ (val[i], wt[i], val[i]/wt[i]) for i in range(N) ]
        max_profit[0] = 0
        for weight in range(1,W+1):
            optimum = 0
            for i in range(N):
                if wt[i] > weight:
                    continue
                value = val[i] + max_profit[weight-wt[i]]
                if value > optimum:
                    optimum = value
            max_profit[weight] = optimum
        return max_profit[W]
