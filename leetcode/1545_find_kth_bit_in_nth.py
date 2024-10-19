class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        bin_str = [0]
        for i in range(2,n+1):
            print ( bin_str )
            ext = [ (1-bin_str[j]) for j in range(len(bin_str)-1,-1,-1) ]
            bin_str.append(1)
            bin_str = bin_str + ext
        print ( bin_str )
        return bin_str[k-1]

s = Solution()
print ( s.findKthBit(3, 1) )
