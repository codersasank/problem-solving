class Solution:
    def deleteMid(self,head):
        if head.next is None:
            return None
        cnt = 0 ; cur = head
        while cur is not None:
            cnt += 1
            cur = cur.next
        mid  = cnt//2 + 1
        cur = head.next ; idx = 2 ; prev = head
        while idx != mid:
            idx += 1
            prev = cur
            cur = cur.next
        prev.next = cur.next
        return head
