class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        idx = dict()
        for i in range(len(nums)):
            num = nums[i]
            if num in idx:
                if (i-idx[num]) <= k:
                    return True
                else:
                    idx[num] = i
            else:
                idx[num] = i 
        return False
