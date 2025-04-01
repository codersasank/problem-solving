class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        points = [ 0 for i in range(n+1)]
        ahead = questions[0][1] + 1
        if ahead < n:
            points[ahead] = questions[0][0]
        else:
            points[n] = questions[0][0]
        for i in range(1,n):
            points[i] = max( points[i], points[i-1] )
            ahead = i + questions[i][1] + 1
            if ahead < n:
                points[ahead] = max( points[ahead] , points[i] + questions[i][0] )
            else:
                points[n] = max( points[n], points[i] + questions[i][0] )
        return max(points)

        
