class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        visited = dict()
        cur = head
        while cur is not None:
            if cur in visited:
                return True
            visited[cur] = True
            cur = cur.next
        return False
