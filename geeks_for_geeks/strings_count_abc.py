class Solution:
    def countStr(self, n):
        permut = 1 + 2*n + n*(n-1) + (n*(n-1))//2 + (n*(n-1)*(n-2))//2
        return permut
