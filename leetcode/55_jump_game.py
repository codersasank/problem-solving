class Solution:
    def canJump(self, nums: List[int]) -> bool:
        position = nums[0]
        n = len(nums)
        if nums[0] >= n-1:
            return True
        for i in range(n-1):
            if i > position:
                return False
            position = max(position, i+nums[i])
        if position < n-1:
            return False
        return True

        
