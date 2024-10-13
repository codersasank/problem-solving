class Solution:
    def printSequence(self,S):
        char_rep = dict()
        num = 1
        for i in range(18):
            if i%3==0:
                num += 1
            char_rep[chr(ord('A')+i)] = str(num)* (i%3 + 1)
        char_rep['S'] = '7777'
        for i in range(19, 25):
            if i%3==1:
                num += 1
            char_rep[chr(ord('A')+i)] = str(num)* ((i-1)%3 + 1)
        char_rep['Z'] = '9999'
        char_rep[' '] = '0'
        
        ret = list()
        for ch in S:
            ret.append(char_rep[ch])
        return "".join(ret)
