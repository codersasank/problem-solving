class Solution:
    def reverseBits(self, n: int) -> int:
        mul = 2**31
        i = 31
        out_ = 0
        for i in range(31, -1, -1):
            bit = n & 1
            out_ += (bit * mul)
            mul //= 2
            n = n >> 1
        return out_
