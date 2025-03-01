class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min_cost = [0 for i in range(len(cost)+1)]
        for i in range(2, len(min_cost)):
            min_cost[i] = min(min_cost[i-1] + cost[i-1], min_cost[i-2] + cost[i-2])
        return min_cost[-1]
