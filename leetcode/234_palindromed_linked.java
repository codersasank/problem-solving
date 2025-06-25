class Solution {
    public boolean isPalindrome(ListNode head) {
        ListNode cur = head;
        ListNode front, rear, prev;
        int size = 0, i=1;
        while (cur!= null){
            size++;
            cur = cur.next;
        }
        if (size==1)
            return true;
        else if (size==2)
            return head.val == head.next.val;
        else if (size==3)
            return head.val == head.next.next.val;
        prev = head;
        cur = head.next;
        prev.next = null;
        while(i!=size/2){
            ListNode nxt = cur.next;
            cur.next = prev;
            prev = cur;
            cur = nxt;
            i++;
        }
        front = prev;
        if (size%2==0)
            rear = cur;
        else
            rear = cur.next;
        while (front!=null){
            if (front.val != rear.val)
                return false;
            front = front.next;
            rear = rear.next;
        }
        return true;
    }
}
