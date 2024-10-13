class Solution:
    def deleteAlt(self, head):
        if head.next is None:
            return head
        i = 1
        prev = head
        cur = head.next
        while cur is not None:
            i += 1
            if i%2==0:
                cur = cur.next
                continue
            prev.next = cur
            prev = cur
            cur = cur.next
        prev.next = cur
        return head
