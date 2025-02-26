class Solution:
    def find_peak(self, nums, left, right):
        if left > right:
            return None
        mid = (left + right)//2
        if (nums[mid] > nums[mid-1]) and (nums[mid] > nums[mid+1]):
            return mid
        elif (nums[mid] < nums[mid-1]):
            return self.find_peak(nums, left, mid-1)
        elif (nums[mid] < nums[mid+1]):
            return self.find_peak(nums, mid+1, right)
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[n-1] > nums[n-2]:
            return n-1
        return self.find_peak(nums, 0, n-1)
