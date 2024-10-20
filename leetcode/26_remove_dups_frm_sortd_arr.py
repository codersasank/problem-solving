class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return 1
        left = right = 1
        prev = nums[0]
        while right<n:
            while right<n and nums[right]==prev:
                right += 1
            if right==n:
                return left
            print ( prev, left, right )
            nums[left] = nums[right]
            prev = nums[left]
            left += 1
        return left
