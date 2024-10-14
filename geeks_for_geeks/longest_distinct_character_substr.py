class Solution:
    def longestSubstrDistinctChars(self, S):
        max_len = 1
        idx = dict()
        n = len(S)
        left = right = idx[S[-1]] = n-1
        while left>0:
            while left-1>=0 and S[left-1] not in idx:
                left -= 1
                idx[S[left]] = left
            #print ( S[left:right+1] )
            temp_len = right-left + 1
            if temp_len > max_len:
                max_len = temp_len
            if left==0:
                break
            left -= 1
            right_tmp = idx[S[left]] - 1
            for i in range(right, idx[S[left]]-1, -1):
                del idx[S[i]]
            right = right_tmp
            idx[S[left]] = left
        return max_len
