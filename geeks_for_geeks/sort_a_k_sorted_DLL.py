import heapq
class Solution:
    def sortAKSortedDLL(self, head, k):
        if k==0:
            return head
        pq = list()
        heapq.heapify(pq)
        cur = head
        cnt = 0
        while cnt<=k and cur is not None:
            heapq.heappush(pq, (cur.data, cnt, cur) )
            cur = cur.next
            cnt += 1
        new_head = heapq.heappop(pq)[2]
        prev = new_head
        if new_head.prev is not None:
            new_head.prev.next = new_head.next
            if new_head.next is not None:
                new_head.next.prev = new_head.prev
            new_head.next = head
            head.prev = new_head
        while pq:
            if cur is not None:
                heapq.heappush(pq, (cur.data, cnt, cur) )
                cnt += 1
                cur = cur.next
            least = heapq.heappop(pq)[2]
            if least.prev is prev:
                prev = least
                continue
            least.prev.next = least.next
            if least.next is not None:
                least.next.prev = least.prev
            tmp = prev.next
            prev.next = least
            least.prev = prev
            least.next = tmp
            tmp.prev = least
            prev = least
        prev.next = None
        return new_head
