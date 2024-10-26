class Solution:
    def maximumMeetings(self,start,end):
        cnt = 1
        n = len(start)
        meetings = [ (start[i], end[i]) for i in range(n) ]
        meetings.sort(key=lambda x:x[1])
        end_time = meetings[0][1]
        for i in range(1,n):
            if meetings[i][0] > end_time:
                cnt += 1
                end_time = meetings[i][1]
        return cnt
