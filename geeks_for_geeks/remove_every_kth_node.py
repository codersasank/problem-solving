class Solution:
    def deleteK(self, head, k):
        if k==1:
            return None
        if head.next is None:
            return head
        cnt = 0 ; cur = head
        while cur is not None:
            cnt += 1
            cur = cur.next
        cur = head.next ; prev = head ; idx = 2
        while cur is not None:
            if idx%k==0:
                prev.next = cur.next
                cur = cur.next
            else:
                prev = cur
                cur = cur.next
            idx += 1
        return head
