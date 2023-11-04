class Solution:
    def minDist(self, arr, n, x, y):
        pair = (x,y) ; cur = 0 ; low_idx = 0
        for i in range(n):
            if arr[i]==x:
                low_idx = i ; break
            elif arr[i]==y:
                cur = 1 ; low_idx = i; break
            else:
                pass
        high_idx = low_idx +1 ; min_diff = None
        try:
            min_diff = abs(arr.index(x)-arr.index(y))
        except:
            return -1
        while high_idx<n:
            if pair[cur]==arr[high_idx]:
                low_idx = high_idx
            elif pair[(cur+1)%2]==arr[high_idx]:
                diff = high_idx - low_idx
                if diff < min_diff:
                    min_diff = diff
                low_idx = high_idx ; cur = (cur+1)%2
            else:
                pass
            high_idx += 1
        return min_diff
