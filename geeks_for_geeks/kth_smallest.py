class Solution:
    def kthSmallest(self, arr,k):
        max_elem = max(arr)
        sorted_arr = list()
        freq = [0 for i in range(max_elem)]
        for num in arr:
            freq[num-1] += 1
        for i in range(max_elem):
            for j in range(freq[i]):
                sorted_arr.append(i+1)
        return sorted_arr[k-1]
