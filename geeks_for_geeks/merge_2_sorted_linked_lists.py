class Solution:
    def mergeResult(self, h1, h2):
        if h1 is None and h2 is None:
            return None
        elif h2 is None or (h1 is not None and (h1.data <= h2.data)):
            head = h1
            merged = h1
            h1 = h1.next
        else:
            head = h2
            merged = h2
            h2 = h2.next
        cur1 = h1 ; cur2 = h2
        while cur1 is not None and cur2 is not None:
            if cur1.data <= cur2.data:
                merged.next = cur1
                merged = cur1
                cur1 = cur1.next
            else:
                merged.next = cur2
                merged = cur2
                cur2 = cur2.next
        if cur1 is None and cur2 is None:
            merged.next = None
        elif cur1 is None:
            merged.next = cur2
        elif cur2 is None:
            merged.next = cur1
        else:
            merged.next = None
        cur = head ; prev = None
        while cur is not None:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev
