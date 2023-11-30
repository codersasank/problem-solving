class Solution:
    def calc(self, n):
        if n<3:
            return n-1
        else:
            return (n%3) + 1 + self.calc(n//3)
    def minimumStep (self, n):
        return self.calc(n)
