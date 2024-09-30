class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1 = len(word1)
        n2 = len(word2)
        ret = list()
        for i in range(min(n1,n2)):
            ret.append(word1[i])
            ret.append(word2[i])
        if n1<=n2:
            for i in range(n1, n2):
                ret.append(word2[i])
        else:
            for i in range(n2, n1):
                ret.append(word1[i])
        return "".join(ret)
        
