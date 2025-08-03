class Solution {
    private class Tuple{
        protected TreeNode node;
        protected Tuple parent;
        protected Tuple(TreeNode node, Tuple parent){
            this.node = node;
            this.parent = parent;
        }
    }
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        TreeNode goalNode=null;
        Tuple firstAncestor=null, goalAncestor=null, top;
        boolean setFirst = false, setGoal=false;
        Stack<Tuple> stack = new Stack<>();
        HashMap<Tuple, Boolean> visited = new HashMap<>();
        stack.add ( new Tuple(root, null) );
        while (stack.size()!=0){
            top = stack.peek();
            if (visited.containsKey(top)){
                stack.pop();
                if (setFirst){
                    if (firstAncestor.parent==top) firstAncestor = top;
                    if (setGoal){
                        if (goalAncestor.parent==top)
                            goalAncestor = top;
                        if (firstAncestor == goalAncestor) return firstAncestor.node;
                    }
                }
                continue;
            }
            if (!setFirst){
                if (top.node == p){
                    goalNode = q;
                    firstAncestor = top;
                    setFirst = true;
                }
                else if (top.node == q){
                    goalNode = p;
                    firstAncestor = top;
                    setFirst = true;
                }
            }
            else if (goalNode==top.node) {
                goalAncestor = top;
                setGoal = true;
            }
            if (top.node.right != null)
                stack.push ( new Tuple(top.node.right, top) );
            if (top.node.left != null)
                stack.push ( new Tuple(top.node.left, top) );
            visited.put(top, true);
        }
        return root;
    }
}
