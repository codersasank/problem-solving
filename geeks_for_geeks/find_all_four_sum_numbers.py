class Solution:
    def fourSum(self, arr, k):
        ret=list()
        A = sorted(arr)
        N = len(A)
        low, high, sump = dict(), dict(), dict()
        for i in range(N-1):
            for j in range(i+1,N):
                low[ (A[i], A[j]) ] = low.get( (A[i], A[j]), (i,j)  )
                high[ (A[i], A[j]) ] = (i, j)
                
        first = sorted( low.keys() )
        for pair in first:
            if sump.get( pair[0] + pair[1] , False)==False:
                sump[pair[0] + pair[1] ] = [ (pair[0], pair[1]) ]
            else:
                sump[pair[0] + pair[1] ].append( (pair[0], pair[1]) )

        for pair_1 in first:
            pair_sum = pair_1[0] + pair_1[1]
            rem = k - pair_sum
            if sump.get(rem, False)==False:
                continue
            for pair_2 in sump[rem]:
                if low[pair_1][1] < high[pair_2][0]:
                    ret.append (( pair_1[0], pair_1[1], pair_2[0], pair_2[1]  ))
        return ret
        
