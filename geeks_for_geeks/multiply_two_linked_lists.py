class Solution:
    def multiply_two_lists(self, first, second):
        divisor = 10**9 + 7
        n1 = n2= 0
        cur = first
        num1 = num2 = 0
        while cur is not None:
            data = cur.data
            num1 = num1*10 + data
            cur = cur.next
        cur = second
        while cur is not None:
            data = cur.data
            num2 = num2*10 + data
            cur = cur.next
        ret = ((num1%divisor)*(num2%divisor))%divisor
        return ret
        
