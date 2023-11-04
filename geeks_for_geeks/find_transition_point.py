class Solution:
    def bsearch(self, arr, low, high):
        if low > high:
            return (-1, -1)
        mid = (low + high)//2
        if arr[mid]==0:
            return self.bsearch(arr, mid+1, high)
        else:
            return (low, mid)
            
    def transitionPoint(self, arr, n):
        low_idx, mid_idx = self.bsearch(arr, 0, n-1)
        if mid_idx==-1:
            return -1
        while mid_idx >= 0:
            prev_idx = mid_idx
            low_idx, mid_idx = self.bsearch(arr, low_idx, mid_idx-1)
        return prev_idx
