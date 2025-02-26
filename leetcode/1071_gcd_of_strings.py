class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        m = len(flowerbed)
        possible = 0
        if n==0:
            return True
        if m==1:
            if flowerbed[0]==0 and n<=1:
                return True
            else:
                return False
        if flowerbed[0]==0 and flowerbed[1]==0:
            flowerbed[0] = 1
            possible += 1
        for i in range(1,m-1):
            if flowerbed[i]==0 and flowerbed[i-1]==0 and flowerbed[i+1]==0:
                flowerbed[i] = 1
                possible += 1
        if flowerbed[m-1]==0 and flowerbed[m-2]==0:
            possible += 1
        if possible >= n:
            return True
        else:
            return False
