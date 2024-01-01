class Solution:
	def editDistance(self, s, t):
	    n1 = len(s) ; n2 = len(t)
	    replacements = [ [0 for j in range(n2+1)] for i in range(n1+1) ]
	    for i in range(n1+1):
	        replacements[i][n2] = n1-i
	    for j in range(n2+1):
	        replacements[n1][j] = n2-j
	    for i in range(n1-1,-1,-1):
	        for j in range(n2-1,-1,-1):
	            if s[i]==t[j]:
	                replacements[i][j] = replacements[i+1][j+1]
	            else:
	                replacements[i][j] = min(replacements[i+1][j+1], replacements[i+1][j], replacements[i][j+1] ) + 1
	    return replacements[0][0]
