class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        left = 1 if s[0]=='0' else 0
        right = 0
        for i in range(1,n):
            if s[i]=='1':
                right += 1
        max_score = left + right
        for i in range(1,n-1):
            if s[i]=='0':
                left += 1
            else:
                right -= 1
            score = left + right
            if score > max_score:
                max_score = score
        return max_score
