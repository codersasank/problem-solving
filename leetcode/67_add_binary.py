class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num_a = num_b = 0
        ret = list()
        for i in range(len(a)-1, -1, -1):
            num_a += (2**(len(a)-1-i)) * int(a[i])
        for i in range(len(b)-1, -1, -1):
            num_b += (2**(len(b)-1-i)) * int(b[i])
        ret_num = num_a + num_b
        while ret_num > 0:
            digit = ret_num % 2
            ret.append(str(digit))
            ret_num //=2
        return "".join(ret[::-1]) if len(ret)!=0 else "0"
