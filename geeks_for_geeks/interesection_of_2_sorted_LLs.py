class Solution:
    def findIntersection(self,head1,head2):
        ll3 = linkedList()
        cur1 = head1; cur2 = head2
        while cur1 is not None and cur2 is not None:
            if cur1.data == cur2.data:
                ll3.insert(cur1.data)
                cur1 = cur1.next ; cur2 = cur2.next
            elif cur1.data<cur2.data:
                cur1 = cur1.next
            else:
                cur2 = cur2.next
        return ll3.head
