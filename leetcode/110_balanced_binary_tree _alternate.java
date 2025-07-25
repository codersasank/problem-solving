class Solution {
    private class Tuple{
        int height;
        boolean balanced;
        protected Tuple(int height, boolean balanced){
            this.height = height;
            this.balanced = balanced;
        }
    }
    private Tuple checkTree(TreeNode node){
        Tuple lSubTree = (node.left==null)?new Tuple(-1, true):checkTree(node.left);
        Tuple rSubTree = (node.right==null)?new Tuple(-1, true):checkTree(node.right);
        boolean balanced = lSubTree.balanced && rSubTree.balanced;
        balanced = balanced && (Math.abs(lSubTree.height-rSubTree.height) <= 1 );
        int height = Math.max(lSubTree.height+1, rSubTree.height+1);
        return new Tuple(height, balanced);
    }
    public boolean isBalanced(TreeNode root) {
        if (root == null)
            return true;
        return checkTree(root).balanced;
    }
}