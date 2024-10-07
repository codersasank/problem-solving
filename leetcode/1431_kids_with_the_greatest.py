class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        n = len(candies)
        result = [False for i in range(n)]
        for i in range(n):
            if candies[i] + extraCandies >= max_candies:
                result[i] = True
        return result
