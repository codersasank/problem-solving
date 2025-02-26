class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        if n == 0 or n == 1:
            return [str(num) for num in nums]
        ranges = list()
        range_len = 0
        for i in range(n):
            if range_len == 0:
                range_str = str(nums[i])
                range_len = 1
            elif nums[i] - 1 != prev:
                if range_len != 1:
                    range_str += "->" + str(prev)
                ranges.append(range_str)
                range_str = str(nums[i])
                range_len = 1
            else:
                range_len += 1
            prev = nums[i]
        if range_len != 1:
            range_str += "->" + str(prev)
        ranges.append(range_str)
        return ranges
