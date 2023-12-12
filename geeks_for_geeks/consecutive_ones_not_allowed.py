class Solution:
	def countStrings(self,n):
	    if n==1:
	        return 2
	    divisor = 10**9 + 7
	    end_with_zero = [0 for i in range(n)]
	    end_with_one = [0 for i in range(n)]
	    end_with_zero[0] = 1 ; end_with_one[0] = 1
	    for i in range(1,n):
            end_with_zero[i] = (end_with_zero[i-1]%divisor + end_with_one[i-1]%divisor)%divisor
            end_with_one[i] = end_with_zero[i-1]
        result = (end_with_zero[n-1]%divisor + end_with_one[n-1]%divisor)%divisor
        return result
