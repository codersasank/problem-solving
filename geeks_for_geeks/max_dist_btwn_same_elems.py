class Solution:
    def maxDistance(self, arr):
        n = len(arr)
        first = dict()
        last = dict()
        min_dist = 0
        for i in range(n):
            num = arr[i]
            if num not in first:
                first[num] = i
            last[num] = i
            if last[num] - first[num] > min_dist:
                min_dist = last[num] - first[num]
        return min_dist
