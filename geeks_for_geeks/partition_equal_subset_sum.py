class Solution:
    def equalPartition(self, N, arr):
        sum_arr = sum(arr)
        if sum_arr%2!=0:
            return False
        half = sum_arr//2
        possible = [ [False for j in range(half+1)] for i in range(N+1) ]
        for i in range(N+1):
            possible[i][0] = True
        for i in range(1,N+1):
            for j in range(1,half+1):
                if j<arr[i-1]:
                    possible[i][j] = possible[i-1][j]
                    continue
                elif j==arr[i-1]:
                    possible[i][j] = True
                else:
                    possible[i][j] = possible[i-1][j] or possible[i-1][j-arr[i-1]]
        return possible[N][half]
