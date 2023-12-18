class Solution:
    def gameOfXor(self, N , A):
        multiples = [0 for i in range(N)]
        multiples[0] = N ; xor = 0
        for i in range(1,N):
            multiples[i] = multiples[i-1] -i + N - i 
        for i in range(N):
            if multiples[i]%2!=0:
                xor = xor ^ A[i]
        return xor
