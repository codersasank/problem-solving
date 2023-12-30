class Solution:    
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, W,arr,n):
        weight_cost = [ (item.weight, item.value, item.value/item.weight) for item in arr ]
        value = 0.
        weight_cost.sort(key=lambda x:x[2])
        temp = W ; idx = n-1
        while idx >=0 and temp >0:
            if weight_cost[idx][0] <= temp:
                temp -= weight_cost[idx][0]
                value += weight_cost[idx][1]
                idx -= 1
            else:
                value += weight_cost[idx][2]*temp
                temp = 0
        return value
