import java.util.Stack;
class Solution {
    public boolean isSymmetric(Node root) {
        // Code here
        Stack<Node> stack1 = new Stack<>();
        Stack<Node> stack2 = new Stack<>();
        if(root.left==null && root.right==null)
            return true;
        else if (root.left==null || root.right==null)
            return false;
        HashMap<Node, Boolean> visited = new HashMap<>();
        stack1.push(root.left);
        stack2.push(root.right);
        while(!stack1.isEmpty() && !stack2.isEmpty()){
            Node top1 = stack1.peek();
            Node top2 = stack2.peek();
            if (top1.data != top2.data)
                return false;
            if (visited.containsKey(top1) && visited.containsKey(top2)){
                stack1.pop();
                stack2.pop();
                continue;
            }
            else if (visited.containsKey(top1) || visited.containsKey(top2))
                return false;
            if (top1.left != null)
                stack1.push(top1.left);
            if (top1.right != null)
                stack1.push(top1.right);
            if (top2.right != null)
                stack2.push(top2.right);
            if (top2.left != null)
                stack2.push(top2.left);
            visited.put(top1, true);
            visited.put(top2, true);
        }
        if (stack1.isEmpty() && stack2.isEmpty())
            return true;
        return false;
    }
}
