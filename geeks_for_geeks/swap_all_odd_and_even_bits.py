import math
class Solution:
    def swapBits(self,n):
        bits_required = math.ceil(math.log2(n)) + 1
        mask_len = bits_required if bits_required%2==0 else bits_required+1
        mask1 = 2 * ( 4**( ((mask_len-2)//2) + 1) - 1)//3
        mask2 = mask1 >> 1
        
        #print ( bits_required, mask_len, mask1, mask2 )
        result = ( mask1 & (n<<1) ) | (mask2 & (n>>1))
        
        return result
