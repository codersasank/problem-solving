class Solution {
    private class Tuple{
        TreeNode node, parent;
        protected Tuple(TreeNode node, TreeNode parent){
            this.node = node;
            this.parent = parent;
        }
    }
    private boolean isValid(TreeNode root, int leftLim, int rightLim, boolean lLimFlag, boolean rLimFlag){
        if (root == null) return true;
        boolean leftValidate = (root.left==null) 
        || ((root.left.val<root.val) && ( (! lLimFlag) || (root.left.val>leftLim) ));
        boolean rightValidate = (root.right==null)
         || ((root.right.val>root.val) && ( (! rLimFlag) || (root.right.val<rightLim) ));

        leftValidate = leftValidate && isValid(root.left, leftLim, root.val, lLimFlag, true);
        rightValidate = rightValidate && isValid(root.right, root.val, rightLim, true, rLimFlag);
        return leftValidate && rightValidate;
    }
    public boolean isValidBST(TreeNode root) {
        if (root == null) return true;
        boolean leftValidate = (root.left==null) || (root.left.val<root.val);
        boolean rightValidate = (root.right==null) || (root.right.val>root.val);

        leftValidate = leftValidate && isValid(root.left, 0, root.val, false, true);
        rightValidate = rightValidate && isValid(root.right, root.val, 0, true, false);
        return leftValidate && rightValidate;
    }
}
