class Solution:
    def shuffleArray(self, arr, n):
        half_n = n//2 ; const_1023 = 2**10 - 1
        for i in range(half_n, n):
            arr[i] = (arr[i] << 10) + arr[i-half_n]
        idx = half_n
        for i in range(0,n,2):
            ab = arr[idx]
            a = ab & const_1023 ; b = ab >> 10
            arr[i] = a ; arr[i+1] = b
            idx += 1
