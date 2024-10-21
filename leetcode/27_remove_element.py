class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        right = n-1
        left = 0
        while left<=right:
            if nums[left]!=val:
                left += 1
                continue
            while right>=0 and nums[right]==val:
                right -= 1
            if left>right:
                break
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return left
