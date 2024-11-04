class Solution:
    def climbStairs(self, n: int) -> int:
        ways = [0 for i in range(n+1)]
        ways[0] = 1
        for i in range(1, n+1):
            ways[i] = (ways[i-2] if i>=2 else 0) + (ways[i-1] if i>=1 else 0)
        return ways[n]
