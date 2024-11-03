class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        n = len(sentence)
        if n==1:
            return True
        for i in range(n):
            if sentence[i]==" ":
                if sentence[i-1]!=sentence[(i+1)%n]:
                    return False
        if sentence[n-1] != sentence[0]:
            return False
        return True
