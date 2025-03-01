class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_ = dict()
        reverse_map = dict()
        n = len(s)
        for i in range(n):
            ch_s = s[i]
            ch_t = t[i]
            if ch_s in map_:
                if map_[ch_s] != ch_t:
                    return False
                elif reverse_map[ch_t] != ch_s:
                    return False
            else:
                if ch_t in reverse_map:
                    if reverse_map[ch_t] != ch_s:
                        return False
                else:
                    reverse_map[ch_t] = ch_s        
                map_[ch_s] = ch_t
        return True
