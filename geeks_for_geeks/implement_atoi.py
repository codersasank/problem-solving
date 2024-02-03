class Solution:
    def atoi(self,s):
        digits = {'0':1,'1':1,'2':1,'3':1,'4':1,'5':1,'6':1,'7':1,'8':1,'9':1}
        if s[0] not in digits and s[0]!='-':
            return -1
        n = len(s)
        for i in range(1,n):
            ch = s[i]
            if ch not in digits:
                return -1
        total = 0 ; place_val = 1
        for i in range(n-1,0,-1):
            total += (ord(s[i])-ord('0'))*place_val
            place_val *= 10
        return -total if s[0]=='-' else total+(ord(s[0])-ord('0'))*place_val
