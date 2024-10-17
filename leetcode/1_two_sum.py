class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        first = dict()
        last = dict()
        n = len(nums)
        for i in range(n):
            if nums[i] not in first:
                first[nums[i]] = i
            last[nums[i]] = i
        for i in range(n):
            num = nums[i]
            if target-num in last and first[num]!=last[target-num]:
                return first[num], last[target-num]
