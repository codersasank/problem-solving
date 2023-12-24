from typing import List
class Solution:
    def buyMaximumProducts(self, n : int, k : int, price : List[int]) -> int:
        purchase = [0 for i in range(n)] ; money = k ; total = 0
        limit = [ (price[i],i+1) for i in range(n)]
        limit.sort(key=lambda x:x[0])
        for i in range(n):
            if money==0 or money < limit[i][0]:
                break
            num_stocks = money//limit[i][0]
            if num_stocks > limit[i][1]:
                num_stocks = limit[i][1]
            money -= num_stocks*limit[i][0]
            total += num_stocks
        return total
            
