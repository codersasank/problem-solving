class Solution:
    def insertionSort(self, head):
        if head is None or head.next is None:
            return head
        n = 0 ; cur = head ; prev = None
        while cur is not None:
            n += 1 ; prev = cur ; cur = cur.next
        boundary = prev ; cur = head
        sort_cnt = 1
        while cur is not boundary:
            prev = boundary
            sorted_cur = boundary.next
            nxt_cur = cur.next
            while sorted_cur is not None and cur.data > sorted_cur.data:
                prev = sorted_cur
                sorted_cur = sorted_cur.next
            prev.next = cur ; cur.next = sorted_cur
            sort_cnt += 1 ; cur = nxt_cur
        head = cur = boundary ; sorted_cur = boundary.next
        if head.data <= sorted_cur.data:
            return head
        head = sorted_cur ; prev = None
        while sorted_cur is not None and cur.data > sorted_cur.data:
            prev = sorted_cur
            sorted_cur = sorted_cur.next
        prev.next = cur ; cur.next = sorted_cur
        return head
