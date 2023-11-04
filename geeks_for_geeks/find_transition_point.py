class Solution:
    def bfs(self, arr, low, high):
        if low > high:
            return (-1, -1)
        mid = (low + high)//2
        if arr[mid]==0:
            return self.bfs(arr, mid+1, high)
        else:
            return (low, mid)
            
    def transitionPoint(self, arr, n):
        low_idx, mid_idx = self.bfs(arr, 0, n-1)
        if mid_idx==-1:
            return -1
        while mid_idx >= 0:
            prev_idx = mid_idx
            low_idx, mid_idx = self.bfs(arr, low_idx, mid_idx-1)
        return prev_idx
