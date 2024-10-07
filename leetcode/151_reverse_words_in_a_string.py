class Solution:
    def reverseWords(self, s: str) -> str:
        words = list()
        temp = list()
        for ch in s:
            if ch==" ":
                if not temp:
                    continue
                words.append(''.join(temp))
                temp.clear()
            else:
                temp.append(ch)
        if temp:
            words.append(''.join(temp))
        words = words[::-1]
        return ' '.join(words)
