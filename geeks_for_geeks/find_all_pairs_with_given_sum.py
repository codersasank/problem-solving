class Solution:
    def allPairs(self, A, B, N, M, X):
        dict_B = {num:True for num in B}
        sorted_A = sorted(A)
        ret = list()
        for num in sorted_A:
            if X-num in dict_B:
                ret.append( (num, X-num) )
        return ret
