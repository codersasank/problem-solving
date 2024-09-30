class Solution:
    def rotateby90(self,a, n):
        for i in range(n):
            for j in range(i,n):
                a[i][j], a[j][i] = a[j][i], a[i][j]
        for i in range(n//2):
            for j in range(n):
                a[i][j], a[n-1-i][j] = a[n-1-i][j], a[i][j]
