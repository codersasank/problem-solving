class Solution:
    def add_next_least(self, root, stack):
        if root.right is None:
            return
        temp = root.right
        while temp is not None:
            stack.append(temp)
            temp = temp.left
    def findCommon(self, root1, root2):
        stack_1, stack_2, ret = list(), list(), list()
        temp1 = root1 ; temp2 = root2
        while temp1 is not None:
            stack_1.append(temp1)
            temp1 = temp1.left
        while temp2 is not None:
            stack_2.append(temp2)
            temp2 = temp2.left
        visited = dict()
        while stack_1 and stack_2:
            least_1 = stack_1[-1] ; least_2 = stack_2[-1]
            if visited.get(least_1, False):
                stack_1.pop(-1)
                continue
            if visited.get(least_2, False):
                stack_2.pop(-1)
                continue
            if least_1.data==least_2.data:
                ret.append(least_1.data)
                visited[least_1]=True ; visited[least_2] = True
                self.add_next_least(least_1, stack_1) ; self.add_next_least(least_2, stack_2)
            elif least_1.data<least_2.data:
                visited[least_1]=True
                self.add_next_least(least_1, stack_1)
            else:
                visited[least_2]=True
                self.add_next_least(least_2, stack_2)
        return ret
            
