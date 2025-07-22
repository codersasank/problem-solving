class MinStack {
    private class Node{
        int val, min;
        Node next;
        public Node(int val){
            this.val = val;
            this.min = val;
            this.next = null;
        }
    }
    int size;
    Node head;
    public MinStack() {
        size = 0;
        head = null;
    }
    
    public void push(int val) {
        Node nxt = head;
        head = new Node(val);
        head.next = nxt;
        if (size==0)
            head.min = val;
        else if (head.next.min < head.min)
            head.min = head.next.min;
        size += 1;
    }
    
    public void pop() {
        int val = head.val;
        head = head.next;
        size -= 1;
    }
    
    public int top() {
        return head.val;
    }
    
    public int getMin() {
        return head.min;
    }
}
