class Solution {
    public boolean isValidBST(TreeNode root) {
        List<Integer> list = new ArrayList<>();
        Stack<TreeNode> stack = new Stack<>();
        HashMap<TreeNode, Boolean> visited = new HashMap<>();
        stack.push(root);
        while (stack.size()!=0){
            TreeNode top = stack.pop();
            if (visited.containsKey(top)){
                list.add(top.val);
                visited.remove(top);
                continue;
            }
            if (top.right!=null) stack.push(top.right);
            stack.push(top);
            if (top.left!=null) stack.push(top.left);
            visited.put(top, true);
        }
        for (int i=0; i<list.size()-1; i++){
            if (list.get(i) >= list.get(i+1))
                return false;
        }
        return true;
    }
}
