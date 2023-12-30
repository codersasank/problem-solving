class Solution:
    #Function to return the largest possible number of n digits
    #with sum equal to given sum.
    def largestNum(self,n,s):
        temp = s ; ret = list()
        for i in range(n):
            if temp>=9:
                ret.append('9')
                temp -= 9
            elif temp>0:
                ret.append(str(temp))
                temp = 0
            else:
                ret.append('0')
        if temp > 0:
            return "-1"
        else:
            return ''.join(ret)
                
        
