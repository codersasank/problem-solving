class Solution:
    def minSubset(self, A,N):
        A.sort(reverse=True)
        total = sum(A)
        sub_sum = 0
        cnt = 0
        for i in range(N):
            sub_sum += A[i]
            total -= A[i]
            cnt += 1
            if sub_sum > total:
                break
        return cnt
