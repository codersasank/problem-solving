class Solution:
	def findMaxSum(self,arr, n):
	    chosen = [0 for i in range(n)]
	    not_chosen = [0 for i in range(n)]
	    chosen[0] = arr[0] ; not_chosen[0] = 0
	    for i in range(1,n):
	        chosen[i] = not_chosen[i-1] + arr[i]
	        not_chosen[i] = max ( chosen[i-1], not_chosen[i-1] )
	    return max(chosen[n-1], not_chosen[n-1])
