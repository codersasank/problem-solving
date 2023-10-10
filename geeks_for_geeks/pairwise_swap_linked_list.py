class Solution:    
    def pairWiseSwap(self, head):
        n = 0
        temp = head
        while temp is not None:
            temp = temp.next
            n += 1
        cnt = 1
        temp = head
        prev = None
        new_head = head
        while cnt<n:
            if prev is None:
                new_head = temp.next
                temp.next = temp.next.next
                new_head.next = temp
                prev = temp
                temp = temp.next
                cnt += 2
                continue
            else:
                prev.next = temp.next
                temp.next = temp.next.next
                prev.next.next = temp
                prev = temp
                temp = temp.next
                cnt += 2
                continue
        return new_head
