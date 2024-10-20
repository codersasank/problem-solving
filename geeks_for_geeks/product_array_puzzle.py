class Solution:
    def productExceptSelf(self, nums):
        prod = 1
        freq = dict()
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            if num==0:
                continue
            prod *= num
        prod_arr = [0 for i in range(len(nums))]
        if freq.get(0, 0) >1:
            return prod_arr
        elif freq.get(0,0)==1:
            prod_arr[ nums.index(0) ] = prod
            return prod_arr
        for i in range(len(nums)):
            prod_arr[i] = prod//nums[i]
        return prod_arr
