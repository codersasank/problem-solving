class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        num_strings = len(strs)
        lengths = [len(string) for string in strs]
        min_length = min(lengths)
        i = 0
        no_common = True
        while i < min_length:
            flag = True
            ch = strs[0][i]
            for string in strs:
                if string[i] != ch:
                    flag = False
                    break
            if flag:
                no_common = False
                i += 1
            else:
                break
        if no_common:
            return ""
        else:
            return strs[0][:i]
