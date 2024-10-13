class Solution:
    def isRotated(self,str1,str2):
        n = len(str1)
        m = len(str2)
        if n!=m:
            return False
        flag = True
        for i in range(n):
            if str1[(i-2)%n] != str2[i]:
                flag = False
                break
        if flag:
            return True
        flag = True
        for i in range(n):
            if str1[(i+2)%n] != str2[i]:
                flag = False
                break
        if flag:
            return True
        else:
            return False
