class Solution:
    def nextLargerElement(self,arr,n):
        stack = list()
        next_greatest = [-1 for i in range(n)]
        for i in range(n-1,-1,-1):
            while stack and stack[-1]<=arr[i]:
                stack.pop(-1)
            if stack:
                next_greatest[i] = stack[-1]
            stack.append(arr[i])
        return next_greatest
