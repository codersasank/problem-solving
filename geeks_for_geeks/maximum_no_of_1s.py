class Solution:
    def bsearch(self, arr, left, right):
        if left>right:
            return None
        mid = (left + right)//2
        if arr[mid]==0 and arr[mid+1]==1:
            return mid
        if arr[mid]==1:
            right = mid-1
        else:
            left = mid+1
        return self.bsearch(arr,left,right)
        
    def maxOnes (self, Mat, N, M):
        ret = 0
        if M==1:
            for i in range(N):
                if Mat[i][0]==1:
                    return i
            return 0
        max_ones_idx = 0
        max_ones = 0
        for i in range(N):
            arr = Mat[i]
            if arr[0]==1:
                return i
            if arr[-1]==0:
                continue
            idx = self.bsearch(arr,0,M-1)
            if M-idx-1 > max_ones:
                max_ones = M-idx-1
                max_ones_idx = i
        return max_ones_idx
