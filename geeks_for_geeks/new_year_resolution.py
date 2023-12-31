from typing import List

class Solution:
    def isPossible(self, N : int, coins : List[int]) -> bool:
        sum_of_coins = sum(coins)
        possible = [ [False for j in range(N+1) ] for i in range(sum_of_coins+1) ]
        possible[0][0] = True
        for j in range(N):
            for i in range(sum_of_coins+1):
                num_coins = coins[j]
                if possible[i][j]:
                    possible[i+num_coins][j+1] = True
                    possible[i][j+1] = True
        for i in range(1,sum_of_coins+1):
            if possible[i][N] and ((i%20==0) or (i%24==0) or i==2024):
                return True
        return False
