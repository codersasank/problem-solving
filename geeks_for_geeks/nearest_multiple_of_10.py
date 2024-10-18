class Solution:
    def roundToNearest (self, s) :
        n = len(s)
        lst = list(s)
        if int(lst[-1]) not in range(6):
            i = n-2
            while lst[i]=="9":
                lst[i] = "0"
                i -= 1
            lst[i] = str ( int(lst[i]) + 1 )
        lst[-1] = "0"
        return "".join(lst)
