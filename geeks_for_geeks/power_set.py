class Solution:
	def AllPossibleStrings(self, s):
	    n = len(s)
	    ret = list()
	    for i in range(1,2**n):
	        num = i
	        temp_str = list()
	        for j in range(n):
	            bit = num%2
	            if bit==1:
	                temp_str.append(s[j])
	            num = num>>1
	        temp_str = ''.join(temp_str)
	        ret.append(temp_str)
	    return sorted(ret)
	            
	            
