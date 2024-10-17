class Solution:
    def maximumSwap(self, num: int) -> int:
        temp = num
        lst = list()
        while temp > 0:
            digit = temp%10
            lst.append(digit)
            temp //= 10
        lst = lst[::-1]
        n = len(lst)
        sorted_lst = list()
        freq = dict()
        for digit in lst:
            freq[digit] = freq.get(digit, 0) + 1
        sorted_lst = [ digit for digit in range(9,-1,-1) for i in range(freq.get(digit,0)) ]
        j = 0
        for i in range(n):
            if lst[i] == sorted_lst[j]:
                j += 1
                i += 1
            else:
                idx = n-1
                while idx>i:
                    if lst[idx]==sorted_lst[j]:
                        break
                    idx -= 1
                lst[i], lst[idx] = lst[idx], lst[i]
                break
        ret = 0
        for i in range(n):
            ret = ret*10 + lst[i]
        return ret

sol = Solution()
ret = sol.maximumSwap(int(input()))
print ( ret )
