class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        stack1, stack2 = [root], [root]
        visited1, visited2 = dict(), dict()
        while stack1 and stack2:
            top1 = stack1[-1]
            top2 = stack2[-1]
            if (top1 is None and top2 is not None) or (top1 is not None and top2 is None):
                return False
            if (top1 is None and top2 is None):
                stack1.pop(-1)
                stack2.pop(-1)
                continue
            if top1.val != top2.val:
                return False
            if top1 in visited1 and top2 in visited2:
                stack1.pop(-1)
                stack2.pop(-1)
                continue
            stack1.append(top1.right)
            stack2.append(top2.left)
            stack2.append(top2.right)
            stack1.append(top1.left)
            visited1[top1] = True
            visited2[top2] = True
        if not stack1 and not stack2:
            return True
        else:
            return False
