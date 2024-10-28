class Solution:
    def removeDuplicates(self, arr):
        unique = [0 for i in range(101)]
        ret = list()
        for num in arr:
            if unique[num]==0:
                unique[num] = 1
                ret.append(num)
        return ret
