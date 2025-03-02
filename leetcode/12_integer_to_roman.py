class Solution:
    def __init__(self):
        self.symbols = [ ('I', 1), ('V', 5), ('X', 10), ('L', 50), ('C', 100), ('D', 500), ('M', 1000) ]
        self.sub_symbols = [ ('IV', 4), ('IX', 9), ('XL', 40), ('XC', 90), ('CD', 400), ('CM', 900)]
    def get_largest_symbol(self, num):
        temp = num
        digit = 0
        while temp > 0:
            digit = temp % 10
            temp = temp // 10
        if digit == 4 or digit == 9:
            idx = len(self.sub_symbols)-1
            while idx >= 0:
                if self.sub_symbols[idx][1] <= num:
                    return self.sub_symbols[idx]
                idx -=1 
        else:
            idx = len(self.symbols)-1
            while idx >= 0:
                if self.symbols[idx][1] <= num:
                    return self.symbols[idx]
                idx -= 1

    def intToRoman(self, num: int) -> str:
        output = list()
        while num > 0:
            ret = self.get_largest_symbol(num)
            symbol, sub = ret
            output.append(symbol)
            num -= sub
        return "".join(output)
