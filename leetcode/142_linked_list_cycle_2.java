public class Solution {
    public ListNode detectCycle(ListNode head) {
        if (head==null || head.next == null)
            return null;
        HashMap<ListNode, Boolean> presence = new HashMap<>();
        ListNode cur = head;
        while (cur != null){
            if (presence.containsKey(cur))
                return cur;
            presence.put(cur, true);
            cur = cur.next;
        }
        return null;
    }
}
