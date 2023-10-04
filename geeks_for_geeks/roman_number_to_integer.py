class Solution:
    def romanToDecimal(self, S):
        n = len(S)
        val = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000 }
        total = 0
        for i in range(n-1,-1,-1):
            if i==n-1 or val[S[i]]>=val[S[i+1]]:
                total += val[S[i]]
            else:
                total -= val[S[i]]
        return total
