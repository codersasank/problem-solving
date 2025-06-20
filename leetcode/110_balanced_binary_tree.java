class Solution {
    public int getHeight(TreeNode node){
        if (node==null) return 0;
        if (node.left == null && node.right == null) return 1;
        int leftHeight = getHeight(node.left);
        int rightHeight = getHeight(node.right);
        if( leftHeight==-1 || rightHeight==-1 || Math.abs(leftHeight - rightHeight) > 1)
            return -1;
        return Math.max(leftHeight, rightHeight)+1;
    }
    public boolean isBalanced(TreeNode root) {
        return this.getHeight(root) != -1;
    }
}
