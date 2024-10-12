class Solution:
    def pairWithMaxSum(self, arr):
        n = len(arr)
        if n==1:
            return -1
        max_sum = 0
        for i in range(n-1):
            if arr[i]+arr[i+1] > max_sum:
                max_sum = arr[i] + arr[i+1]
        return max_sum
