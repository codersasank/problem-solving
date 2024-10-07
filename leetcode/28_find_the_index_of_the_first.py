class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_needle = len(needle)
        offset = 0
        for i in range(len(haystack)-len_needle + 1):
            while offset<len_needle and haystack[i+offset]==needle[offset]:
                offset += 1
            if offset==len_needle:
                return i
            else:
                offset = 0
        return -1
