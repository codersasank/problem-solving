import heapq
class Solution:
   def minCost(self, arr) -> int:
       heapq.heapify(arr)
       cost = 0
       while arr:
           a = heapq.heappop(arr)
           if not arr:
               return cost
           b = heapq.heappop(arr)
           cost += a+b
           heapq.heappush(arr, a+b)
       return cost     
                
