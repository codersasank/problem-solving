class Solution:
	def countPairsWithDiffK(self,arr, k):
		ret = 0
		occurences = dict()
		n = len(arr)
		for i in range(n):
			if arr[i] not in occurences:
				occurences[arr[i]] = [i]
			else:
				occurences[arr[i]].append(i)
		for num in occurences:
		    occurences[num] = occurences[num][::-1]
		for i in range(n):
			if arr[i]-k >=0:
				if arr[i]-k in occurences:
					ret += len(occurences[arr[i]-k])
			if arr[i]+k in occurences:
			    ret += len(occurences[arr[i]+k])
			occurences[arr[i]].pop(-1)
		return ret
