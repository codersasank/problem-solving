class Solution:
    def matrixDiagonally(self,mat):
        n = len(mat[0])
        ret = [ mat[0][0] ] 
        if n==1:
            return ret
        elif n==2:
            return [mat[0][0], mat[0][1], mat[1][0], mat[1][1]]
        start = [0, 1]
        while start[0]<=n-1 and start[1] <= n-1:
            if start[0]<=start[1]:
                inc_row = True
            else:
                inc_row = False
            while ((inc_row and start[1]>0 and start[0]<=n-1) or (not inc_row and start[1]<n-1 and start[0]>=0)):
                ret.append(mat[start[0]][start[1]])
                if inc_row:
                    start[0] += 1 ; start[1] -=1
                else:
                    start[0] -= 1 ; start[1] +=1
            if start[0]==-1:
                start[0] = 0
            elif start[0]==n:
                start[0] = n-1
                start[1] += 2
                if start[1]==n-1:
                    ret.append(mat[n-1][n-1])
                    return ret
            elif start[1]==0 or start[1]==n-1:
                ret.append(mat[start[0]][start[1]])
                if start[0]==n-1 and start[1]==0 and inc_row:
                    start[1] = 1
                else:
                    start[0] += 1
        return ret
