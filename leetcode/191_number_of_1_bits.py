class Solution:
    def __init__(self):
        self.bits = [0 for i in range(256)]
        for i in range(256):
            temp = i
            cnt = 0
            while temp > 0:
                cnt = cnt+1 if temp & 1 == 1 else cnt
                temp = temp >> 1
            self.bits[i] = cnt
    def hammingWeight(self, n: int) -> int:
        cnt_lst = [0, 0, 0, 0]
        cnt_lst[0] = self.bits[ (n & 0xFF000000)>> (4*6) ]
        cnt_lst[1] = self.bits[ (n & 0x00FF0000)>> (4*4) ]
        cnt_lst[2] = self.bits[ (n & 0x0000FF00)>> (4*2) ]
        cnt_lst[3] = self.bits[ n & 0x000000FF ]
        return sum(cnt_lst)
