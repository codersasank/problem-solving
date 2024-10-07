class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        print(prices)
        if n==1:
            return 0
        max_val = prices[n-1]
        highest_to_right = [0 for i in range(n-1)]
        for i in range(n-2, -1, -1):
            if prices[i+1]>=max_val:
                max_val = prices[i+1]
            highest_to_right[i] = max_val
        print ( highest_to_right )    
        for i in range(n-1):
            highest_to_right[i] = (highest_to_right[i]-prices[i]) if prices[i] < highest_to_right[i] else 0
        print ( highest_to_right ) 
        return max(highest_to_right)

lst = list(map(int, input().split()))
sol = Solution()
ret = sol.maxProfit(lst)
print ( ret )
