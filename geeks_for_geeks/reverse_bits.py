class Solution:
    def reversedBits(self, x):
        ret = 0
        temp = x
        for i in range(32):
            rem = temp%2
            ret += rem*(2**(32-i))
            temp = temp//2
        return ret
