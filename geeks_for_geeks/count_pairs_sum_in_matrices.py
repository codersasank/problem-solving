class Solution:
	def countPairs(self, mat1, mat2, n, x):
	    idx1 = 0 ; idx2 = n*n - 1
	    cnt = 0
	    while idx1<n*n and idx2>=0:
	        while idx2>=0 and ((mat1[idx1//n][idx1%n] +  mat2[idx2//n][idx2%n])>x):
	            idx2 -= 1
	        if idx2==-1:
	            break
	        if mat1[idx1//n][idx1%n] +  mat2[idx2//n][idx2%n]==x:
	            cnt += 1
	            idx1 += 1
	        while idx1<n*n and (mat1[idx1//n][idx1%n] +  mat2[idx2//n][idx2%n]<x):
	            idx1 += 1
	        if idx1==n*n:
	            break
	        if mat1[idx1//n][idx1%n] +  mat2[idx2//n][idx2%n]==x:
	            cnt += 1
	            idx1 += 1
	    return cnt
