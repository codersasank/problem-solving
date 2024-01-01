class Solution:
    def minCoins(self, coins, M, V):
        ways = [0 for i in range(V+1)]
	    min_coin = min(coins)
	    for i in range(1,V+1):
	        if (i-min_coin)<0:
	            ways[i] = -1
	            continue
	        min_val = V + 1
	        for j in range(M):
	            val = ways[i-coins[j]] + 1 if (i>=coins[j] and ways[i-coins[j]]!=-1) else V+1
	            min_val = min(min_val, val)
	        ways[i] = min_val if min_val!=V+1 else -1
	    return ways[V]
	        
