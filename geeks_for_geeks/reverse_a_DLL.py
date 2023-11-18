class Solution:
    def reverseDLL(self, head):
        prev = None ; cur = head
        while cur is not None:
            prev = cur ; nxt = cur.next
            cur.next , cur.prev = cur.prev, cur.next
            cur = nxt
        return prev
        
