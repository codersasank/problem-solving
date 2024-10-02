class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels_dict = {'a':1, 'A':1, 'e':1, 'E':1, 'i':1, 'I':1, 'o':1, 'O':1, 'u':1, 'U':1}
        str_as_list = list(s)
        n = len(s)
        left = 0
        right = n-1
        while left<right:
            while left<n and s[left] not in vowels_dict:
                left += 1
            while right>=0 and s[right] not in vowels_dict:
                right -= 1
            if left>=right:
                break
            str_as_list[left], str_as_list[right] = str_as_list[right], str_as_list[left]
            left += 1
            right -= 1
        return ''.join(str_as_list)
