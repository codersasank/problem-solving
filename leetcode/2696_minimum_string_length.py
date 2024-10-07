class Solution:
    def minLength(self, s: str) -> int:
        stack = list()
        for ch in s:
            if not stack:
                stack.append(ch)
                continue
            top = stack[-1]
            if (top=='A' and ch=='B') or (top=='C' and ch=='D'):
                stack.pop(-1)
                continue
            stack.append(ch)
        return len(stack)
        
