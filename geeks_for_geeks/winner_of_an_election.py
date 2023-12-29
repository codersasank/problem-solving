class Solution:
    def winner(self,arr,n):
        votes = dict()
        for cand in arr:
            votes[cand] = votes.get(cand, 0) + 1
        max_cnt = votes[arr[0]]
        name = arr[0]
        for cand in votes:
            cnt = votes[cand]
            if cnt>max_cnt or (cnt==max_cnt and cand<name):
                max_cnt = cnt ; name = cand
                
        return [name, str(max_cnt)]
