class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[0])
        n = len(points)
        max_diff = points[1][0]-points[0][0]
        for i in range(1,n):
            diff = points[i][0]-points[i-1][0]
            if diff > max_diff:
                max_diff = diff
        return max_diff
        
