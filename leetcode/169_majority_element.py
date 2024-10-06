class Solution:
    def majorityElement(self, nums):
        n = len(nums)
        left = 0
        right = n-1
        frequent = None
        while left<right:
            if nums[left]==nums[right]:
                if not frequent:
                    frequent = (nums[left], 2)
                else:
                    if frequent[0]!=nums[left]:
                        if frequent[1]==2:
                            frequent = None
                        else:
                            frequent = (frequent[0], frequent[1]-2)
                    else:
                        frequent = (frequent[0], frequent[1]+2)
            left += 1
            right -= 1
        if left==right:
            if not frequent:
                return nums[left]
            else:
                return frequent[0]
        return frequent[0]
                
lst = list(map(int, input().split()))
sol = Solution()
ret = sol.majorityElement(lst)
print ( ret )
