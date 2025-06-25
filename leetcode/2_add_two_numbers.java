class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode head = new ListNode(0);
        ListNode cur = head;
        int carry = 0;
        cur.val = l1.val + l2.val;
        carry = cur.val/10;
        cur.val -= carry*10;
        l1 = l1.next; l2 = l2.next;
        while (l1!=null && l2!=null){
            int val = l1.val + l2.val + carry;
            carry = (val/10);
            val -= carry*10;
            cur.next = new ListNode(val);
            cur = cur.next;
            l1 = l1.next; l2 = l2.next;
        }
        while (l1!=null){
            int val = l1.val + carry;
            carry = (val/10);
            val -= carry*10;
            cur.next = new ListNode(val);
            cur = cur.next;
            l1 = l1.next;
        }
        while (l2!=null){
            int val = l2.val + carry;
            carry = (val/10);
            val -= carry*10;
            cur.next = new ListNode(val);
            cur = cur.next;
            l2 = l2.next;
        }
        if (carry!=0){
            cur.next = new ListNode(carry);
            cur = cur.next;
        }
        cur.next = null;
        return head;
    }
}
