class Solution:
    def printClosest (self,arr, brr, n, m, x) : 
        if n>m:
            a, b =  brr, arr
            n_a , n_b = m, n
        else:
            a , b = arr, brr 
            n_a , n_b = n, m
        min_diff = abs( x - ( a[0]+b[0]) )
        min_pts = (a[0], b[0])
        
        for c_b in range(1,n_b):
            diff = abs( x- (a[0]+b[c_b]) )
            if diff<=min_diff:
                min_diff = diff
                min_pts = (a[0], b[c_b])
            else:
                c_b -= 1
                break
        
        for c_a in range(1,n_a):
            diff = abs(x - (a[c_a]+b[c_b]) )
            if diff<min_diff:
                min_diff = diff
                min_pts = (a[c_a], b[c_b])
            while c_b>0:
                new_c_b = c_b -1
                new_diff = abs(x - (a[c_a]+b[new_c_b]) )
                if new_diff<=diff:
                    if new_diff<min_diff:
                        min_diff = new_diff
                        min_pts = (a[c_a], b[new_c_b])
                    diff = new_diff
                    c_b -= 1
                else:
                    break
        return min_pts
