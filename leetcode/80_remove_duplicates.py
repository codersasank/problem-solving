class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ptr1 = ptr2 = 0
        n = len(nums)
        while ptr2 < n-1:
            if nums[ptr2] == nums[ptr2+1]:
                temp = nums[ptr2]
                while ptr2 < n and nums[ptr2] == temp:
                    ptr2 += 1
                nums[ptr1] = nums[ptr1+1] = temp
                ptr1 += 2
                if ptr2 == n:
                    return ptr1
            else:
                nums[ptr1] = nums[ptr2]
                ptr1 += 1
                ptr2 += 1
        if ptr2 == n-1:
            nums[ptr1] = nums[ptr2]
            return ptr1+1
        return ptr1
