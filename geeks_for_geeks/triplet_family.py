class Solution:
    def findTriplet(self, arr):
        n = len(arr)
        arr.sort()
        for i in range(n-2):
            k = i+2
            for j in range(i+1,n-1):
                k = max(j+1, k)
                while k<n and arr[k] < arr[i] + arr[j]:
                    k += 1
                if k==n:
                    break
                if arr[k] == arr[i] + arr[j]:
                    return True
        return False
