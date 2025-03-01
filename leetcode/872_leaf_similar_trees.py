class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        stack1 = [root1]
        stack2 = [root2]
        leaf_seq1 = list()
        leaf_seq2 = list()
        visited = dict()
        while stack1:
            top = stack1[-1]
            if top in visited:
                if top.left is None and top.right is None:
                    leaf_seq1.append(top.val)
                stack1.pop(-1)
                continue
            if top.right is not None:
                stack1.append(top.right)
            if top.left is not None:
                stack1.append(top.left)
            visited[top] = True
        while stack2:
            top = stack2[-1]
            if top in visited:
                if top.left is None and top.right is None:
                    leaf_seq2.append(top.val)
                stack2.pop(-1)
                continue
            if top.right is not None:
                stack2.append(top.right)
            if top.left is not None:
                stack2.append(top.left)
            visited[top] = True
        if leaf_seq1 == leaf_seq2:
            return True
        return False
