class Solution:
    def frequencyCount(self, arr, N, P):
        idx = cnt = 0
        while idx<N:
            if arr[idx]<=0:
                idx += 1
                continue
            j = arr[idx]-1
            if j>=N:
                arr[idx] = 0
                idx += 1
                continue
            temp = arr[j]
            if temp>0:
                arr[idx] = temp
                arr[j] = -1
            else:
                arr[idx] = 0
                arr[j] -= 1
        for i in range(N):
            arr[i] = abs(arr[i])
