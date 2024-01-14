from typing import List
import math

class Solution:
    def max_courses(self, n : int, total : int, cost : List[int]) -> int:
        courses = [ [0 for j in range(total+1)] for i in range(n+1) ]
        for i in range(1,n+1):
            for j in range(1,total+1):
                expense = cost[n-i]-math.floor(0.9*cost[n-i])
                courses[i][j] = max( courses[i-1][j], 1+courses[i-1][j-expense] if j>=cost[n-i] else 0)
        return courses[n][total]
