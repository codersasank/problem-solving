class Solution:
    def findPair(self, n : int, x : int, arr : List[int]) -> int:
        occurence = dict()
        dup = False
        for num in arr:
            if num in occurence:
                dup = True
            occurence[num] = True
        if x==0:
            if dup:
                return 1
            else:
                return -1
        for num in arr:
            if num-x in occurence or num+x in occurence:
                return 1
        return -1
