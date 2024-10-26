class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        right = n-1
        while right>=0 and digits[right]==9:
            digits[right] = 0
            right -= 1
        if right!=-1:
            digits[right] += 1
        else:
            digits = [1] + digits
        return digits
