class Solution:
    def bsearch(self, left, right):
        mid = (left+right)//2
        response = guess(mid)
        if response == 0:
            return mid
        elif response == -1:
            return self.bsearch(left, mid-1)
        else:
            return self.bsearch(mid+1, right)

    def guessNumber(self, n: int) -> int:
        return self.bsearch(1, n)
        
