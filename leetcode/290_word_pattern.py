class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        if len(pattern) != len(words):
            return False
        map_ = dict()
        reverse_map = dict()
        n = len(pattern)
        for i in range(n):
            ch = pattern[i]
            word = words[i]
            if ch in map_:
                if map_[ch] != word:
                    return False
                elif reverse_map[word] != ch:
                    return False
            else:
                if word in reverse_map:
                    if reverse_map[word] != ch:
                        return False
                else:
                    reverse_map[word] = ch
                map_[ch] = word
        return True
