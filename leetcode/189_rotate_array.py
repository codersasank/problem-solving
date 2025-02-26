class Solution:
    def reverse(self, left, right, arr):
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1 
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        if k == 0:
            return
        self.reverse(0, k, nums)
        self.reverse(k+1, n-1, nums)
        left = k - 1
        right = (k + 1)%n
        swaps = 0
        while swaps < n-1:
            nums[left], nums[right] = nums[right], nums[left]
            if left != right:
                swaps += 2
            else:
                swaps += 1
            left = (left - 1)%n
            right = (right + 1)%n
        

