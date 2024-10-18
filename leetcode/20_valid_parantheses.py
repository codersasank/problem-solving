class Solution:
    def isValid(self, s: str) -> bool:
        open_ = { '(':0, '{':1, '[':2 }
        closed = { ')':0, '}':1, ']':2 }
        stack = list()
        for ch in s:
            if not stack or ch in open_:
                stack.append(ch)
                continue
            if stack[-1] in closed:
                return False
            if open_[stack[-1]] != closed[ch]:
                return False
            stack.pop(-1)
        if stack:
            return False
        return True
