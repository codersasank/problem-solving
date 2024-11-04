class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        pattern_dict = dict()
        for string in strs:
            freq = [0 for i in range(26)]
            for ch in string:
                freq[ord(ch)-ord('a')] += 1
            tup = tuple(freq)
            if tup in pattern_dict:
                pattern_dict[tup].append(string)
            else:
                pattern_dict[tup] = [ string ]
        return list(pattern_dict.values())
