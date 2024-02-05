class Solution:
    def sortedInsert(self, head, data):
        new_node = Node(data)
        cur = head
        if head is None:
            new_node.next = new_node
            return new_node
        while cur.next is not head:
            cur = cur.next
        prev = cur ; cur = head
        if data<=head.data:
            prev.next = new_node
            new_node.next = head
            return new_node
        while cur.next is not head:
            if data<=cur.data:
                break
            prev = cur
            cur = cur.next
        if cur.next is head:
            if data>cur.data:
                prev.next = cur
                cur.next = new_node
                new_node.next = head
            else:
                prev.next = new_node
                new_node.next = cur
        else:
            prev.next = new_node
            new_node.next = cur
        return head
