class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n1 = len(str1)
        n2 = len(str2)
        for i in range( min(n1, n2), 0, -1):
            if n1%i == 0 and n2%i == 0:
                prefix1 = str1[:i]
                prefix2 = str2[:i]
                if prefix1 != prefix2:
                    continue
                if (prefix1 * (n1//i) == str1) and (prefix2 * (n2//i) == str2):
                    return prefix1
        return ""
