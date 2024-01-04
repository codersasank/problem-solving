class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freq = dict()
        ops = 0
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        for num in freq:
            if freq[num]==1:
                return -1
        for num in freq:
            temp = freq[num]
            ops += temp//3
            temp %= 3
            if temp==1:
                ops -=1
                temp += 3
            ops += temp//2
        return ops
