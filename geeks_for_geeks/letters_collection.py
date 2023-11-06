class Solution:
    def letters(self, n, m, mat, i, j):
        if i>=0 and i<n and j>=0 and j<m:
            return mat[i][j]
        return 0
    def one_hop_dist(self, n, m, mat, i, j):
        ret = self.letters(n,m,mat,i-1,j-1) + self.letters(n,m,mat,i-1,j) +  self.letters(n,m,mat,i-1,j+1) + self.letters(n,m,mat,i,j-1) + self.letters(n,m,mat,i,j+1) + self.letters(n,m,mat,i+1,j-1) + self.letters(n,m,mat,i+1,j) + self.letters(n,m,mat,i+1,j+1) 
        return ret
    def two_hop_dist(self, n, m, mat, i, j):
        two_hop_sum = 0
        for r in range(i-2, i+3):
            if r==i-2 or r==i+2:
                for c in range(j-2, j+3):
                    two_hop_sum += self.letters(n,m,mat,r,c)
            else:
                two_hop_sum += self.letters(n,m,mat,r,j-2) + self.letters(n,m,mat,r,j+2)
        return two_hop_sum
    def matrixSum(self, n, m, mat, q, queries):
        ret = list()
        for k in range(q):
            q_type , i , j = queries[k]
            if q_type==1:
                ret.append(self.one_hop_dist(n,m,mat,i,j))
            else:
                ret.append(self.two_hop_dist(n,m,mat,i,j))
        return ret
                
            
