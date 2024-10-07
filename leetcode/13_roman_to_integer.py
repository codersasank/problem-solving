class Solution:
    def romanToInt(self, s: str) -> int:
        value = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        n = len(s)
        total = 0
        for i in range(n-1):
            if value[s[i]] >= value[s[i+1]]:
                total += value[s[i]]
            else:
                total -= value[s[i]]
        total += value[s[n-1]]
        return total
