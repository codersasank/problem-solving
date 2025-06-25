public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        ListNode cur = headB;
        while (cur != null){
            cur.val = -cur.val;
            cur = cur.next;
        }
        cur = headA;
        while(cur!=null){
            if (cur.val < 0)
                break;
            cur = cur.next;
        }
        while (headB != null){
            headB.val = -headB.val;
            headB = headB.next;
        }
        return cur;
    }
}
