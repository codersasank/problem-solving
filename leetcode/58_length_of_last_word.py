class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        count = 0
        began = False
        for i in range(n-1, -1, -1):
            ch = s[i]
            if ch == " ":
                if began:
                    return count
                else:
                    continue
            else:
                began = True
                count += 1
        return count
