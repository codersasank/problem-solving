class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        unique_dict = dict()
        for num in arr:
            if num not in unique_dict:
                unique_dict[num] = 1
        unique_list = list()
        unique_list = sorted([num for num in unique_dict])
        n = len(unique_list)
        rank_dict = {unique_list[i]:i+1 for i in range(n)}
        for i in range(len(arr)):
            arr[i] = rank_dict[arr[i]]
        return arr
