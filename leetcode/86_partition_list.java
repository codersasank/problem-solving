class Solution {
    public ListNode partition(ListNode head, int x) {
        if (head==null || head.next==null)
            return head;
        ListNode cur = head, new_head=null, min = head, max=head, tail=null;
        boolean foundHead = false;
        int size=0, i=0;
        while (cur != null){
            size++;
            if (cur.val < x && !foundHead){
                new_head = cur;
                foundHead = true;
            }
            if (cur.val < min.val)
                min = cur;
            if (cur.val > max.val)
                max = cur;
            tail = cur;
            cur = cur.next;
        }
        //System.out.printf("min %d, max %d\n", min.val, max.val);
        if (min.val >= x || max.val < x)
            return head;
        cur = head;
        while (cur!=new_head){
            tail.next = cur;
            tail = tail.next;
            cur = tail.next;
            tail.next = null;
            i++;
        }
        while (i<size-1){
            ListNode nxt = cur.next;
            if (nxt==null)
                break;
            if (nxt.val >= x){
                tail.next = nxt;
                tail = tail.next;
                cur.next = tail.next;
                tail.next = null;
            }
            else
                cur = nxt;
            //System.out.printf("%d %d\n", cur.val, tail.val);
            i++;
        }
        return new_head;
    }
}
