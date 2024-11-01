class Solution:
    def maxSum(self,arr):
        new_arr = sorted(arr)
        max_sum = 0
        n = len(arr)
        for i in range(n):
            if i%2==0:
                arr[i] = new_arr[i//2]
            else:
                arr[i] = new_arr[n-(i//2)-1]
        for i in range(n):
            max_sum += abs(arr[i]-arr[(i+1)%n])
        return max_sum
