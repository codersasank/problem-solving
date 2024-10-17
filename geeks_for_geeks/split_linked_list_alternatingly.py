class Solution:
    def alternatingSplitList(self, head):
        if head.next is None:
            return (head, None)
        prev1 = head1 = head
        prev2 = head2 = head1.next
        cur = head2.next
        while cur is not None:
            prev1.next = cur
            if prev2 is not None:
                prev2.next = cur.next
            prev1 = cur
            prev2 = cur.next
            cur = cur.next.next if cur.next is not None else None
        prev1.next = None
        if prev2 is not None:
            prev2.next = None
        return [head1, head2]
