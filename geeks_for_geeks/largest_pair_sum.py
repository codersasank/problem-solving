class Solution:
    def pairsum(self, arr : List[int]) -> int:
        largest = max(arr)
        second_largest = min(arr)
        for num in arr:
            if num==largest:
                continue
            if num > second_largest:
                second_largest = num
        return largest + second_largest
        
