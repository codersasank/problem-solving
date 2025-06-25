class Solution {
    public void deleteNode(ListNode node) {
        ListNode nxt = node.next;
        node.next = nxt.next;
        node.val = nxt.val;
        nxt.next = null;
    }
}
