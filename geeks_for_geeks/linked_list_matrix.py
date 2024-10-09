class Solution:
    def constructLinkedMatrix(self, mat):
        n = len(mat)
        if n==0:
            return None
        elif n==1:
            return Node(mat[0][0])
        heads = list()
        for i in range(n):
            cur = head = Node(mat[i][0])
            head.down = head.right = None
            heads.append(head)
            for j in range(1,n):
                cur.right = Node(mat[i][j])
                cur = cur.right
                cur.down = cur.right = None
        ret = heads[0]
        for j in range(n):
            for i in range(n-1):
                heads[i].down = heads[i+1]
                heads[i] = heads[i].right
            heads[n-1] = heads[n-1].right
        return ret
