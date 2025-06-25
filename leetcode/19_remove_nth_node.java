class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        int size = 0, i=0;
        ListNode cur = head;
        while(cur != null){
            size += 1;
            cur = cur.next;
        }
        if(size==n)
            return head.next;
        cur = head;
        while (i!=size-n-1){
            cur = cur.next;
            i++;
        }
        cur.next = cur.next.next;
        return head;
    }
}
