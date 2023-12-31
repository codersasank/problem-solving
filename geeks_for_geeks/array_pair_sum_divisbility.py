class Solution:
    def canPair(self, nums, k):
        freq = dict()
	    for num in nums:
	        rem = num%k
	        if rem==0:
	            continue
	        freq[rem] = freq.get(rem, 0) + 1
	    for rem in freq:
	        if freq.get(rem, 0) != freq.get(k-rem, 0):
	            return False
	    return True
	            
	    
