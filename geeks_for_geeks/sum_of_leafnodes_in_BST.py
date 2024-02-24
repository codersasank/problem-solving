class Solution:
    def sumOfLeafNodes(self, root):
        stack = [[root, False]]
        total = 0
        while stack:
            top = stack[-1]
            if top[1]:
                stack.pop(-1)
                continue
            left = top[0].left
            right = top[0].right
            if right is None and left is None:
                total += top[0].data
                stack.pop(-1)
                continue
            if right is not None:
                stack.append([right,False])
            if left is not None:
                stack.append([left,False])
            top[1] = True
        return total
