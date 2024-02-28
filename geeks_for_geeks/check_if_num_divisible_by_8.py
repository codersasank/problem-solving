class Solution:
    def DivisibleByEight(self,s):
        cnt = 1 ; last_3 = ""
        for ch in reversed(s):
            last_3 = ch + last_3
            if cnt==3:
                break
            cnt += 1
        if int(last_3)%8==0:
            return 1
        else:
            return -1
