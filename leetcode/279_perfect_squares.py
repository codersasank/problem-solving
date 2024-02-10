import math
class Solution:
    def numSquares(self, n: int) -> int:
        min_squares = [0]*(n+1)
        sqrt_n = int(math.sqrt(n))
        for i in range(1,sqrt_n+1):
            min_squares[i*i] = 1
        for i in range(1,n+1):
            if min_squares[i]==1:
                continue
            sqrt_i = int(math.sqrt(i))
            min_val = min_squares[i-1] + 1
            for j in range(1,sqrt_i+1):
                val = min_squares[i-j*j] + 1
                if val < min_val:
                    min_val = val
            min_squares[i] = min_val
        return min_squares[n]

