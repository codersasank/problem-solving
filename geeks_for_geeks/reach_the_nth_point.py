class Solution:
	def nthPoint(self,n):
	    divisor = 10**9 + 7
	    ways = [0 for i in range(n+1) ]
	    ways[0] = ways[1] = 1
	    for i in range(1,n+1):
	        ways[i] = ((ways[i-1] if i>=1 else 0)%divisor + (ways[i-2] if i>=2 else 0)%divisor)%divisor
        return ways[n]
        
