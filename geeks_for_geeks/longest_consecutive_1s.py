class Solution:
    def maxConsecutiveOnes(self, N):
        started = False
        max_cnt = cnt = 0
        while N>0:
            bit = N%2
            if started:
                if bit==1:
                    cnt += 1
                else:
                    if cnt > max_cnt:
                        max_cnt = cnt
                    cnt = 0
                    started = False
            else:
                if bit==1:
                    cnt = 1
                    started = True
            N //= 2
        if cnt > max_cnt:
            max_cnt = cnt
        return max_cnt
