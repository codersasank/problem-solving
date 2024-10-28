class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        prev = head
        cur = head.next
        while cur is not None:
            while cur is not None and cur.val == prev.val:
                cur = cur.next
            if cur is None:
                prev.next = None
                return head
            prev.next = cur
            prev = cur
            cur = cur.next
        prev.next = None
        return head
