class Solution:
    def tribonacci(self, n: int) -> int:
        arr = [0 for i in range(38)]
        arr[1] = arr[2] = 1
        if n <=2:
            return arr[n]
        for i in range(3,n+1):
            arr[i] = arr[i-1] + arr[i-2] + arr[i-3]
        return arr[n]
