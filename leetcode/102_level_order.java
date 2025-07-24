class Solution {
    private class Tuple<A>{
        protected A node;
        protected int level;
        protected Tuple(A node, int level){
            this.node = node;
            this.level = level;
        }
    }
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> ret = new ArrayList<List<Integer>>();
        Queue<Tuple<TreeNode>> q = new LinkedList<>();
        if (root==null) return ret;
        q.add(new Tuple<TreeNode>(root, 0));
        while(q.size()!=0){
            Tuple<TreeNode> frontTuple = q.remove();
            if (frontTuple.level >= ret.size())
                ret.add(new ArrayList<Integer>());
            ret.get(frontTuple.level).add(frontTuple.node.val);
            if (frontTuple.node.left != null)
                q.add(new Tuple<TreeNode>(frontTuple.node.left, frontTuple.level+1));
            if (frontTuple.node.right != null)
                q.add(new Tuple<TreeNode>(frontTuple.node.right, frontTuple.level+1));
        }
        return ret;
    }
}
