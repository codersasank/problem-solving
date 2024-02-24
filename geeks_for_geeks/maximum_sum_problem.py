class Solution:
    def get_sum(self, n):
        if n<=4:
            return n
        total = self.get_sum(n//2) + self.get_sum(n//3) + self.get_sum(n//4)
        if total>self.max_sum[n]:
            self.max_sum[n] = total
        return self.max_sum[n]
    def maxSum(self, n):
        self.max_sum = [i for i in range(n+1)]
        return self.get_sum(n)
        
