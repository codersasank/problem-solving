class Solution:
    def terminate(self, first, i):
        if i==0:
            return -1
        else:
            return first[:i]
    def longestCommonPrefix(self, arr, n):
        first = arr[0]
        first_len = len(first)
        for i in range(first_len):
            ch = first[i]
            for j in range(1,n):
                try:
                    if ch!=arr[j][i]:
                        return self.terminate(first,i)
                except:
                    return self.terminate(first,i)
        return self.terminate(first, i+1)
