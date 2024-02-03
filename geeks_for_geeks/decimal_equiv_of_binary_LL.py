class Solution:
    def decimalValue(self, head):
        MOD=10**9+7
        n = 0 ; cur = head
        total = 0
        while cur is not None:
            cur = cur.next
            n += 1
        place_val = (2**(n-1))
        cur = head
        while cur is not None:
            total = (total%MOD + (cur.data%MOD * place_val)%MOD)%MOD
            cur = cur.next
            place_val //= 2
        return total
