class Solution:
	def maxDotProduct(self, n, m, a, b):
	    val = [[0 for i in range(m+1)] for j in range(n+1)]
	    for i in range(1,m+1):
	        for j in range(i,n+1):
	            val[j][i] = max( a[j-1]*b[i-1] + val[j-1][i-1], val[j-1][i] if j-1>=i else 0 )
	    return val[n][m]
