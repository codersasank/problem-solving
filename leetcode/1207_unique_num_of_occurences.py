class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = dict()
        present = dict()
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        for num in freq:
            if freq[num] in present:
                return False
            else:
                present[freq[num]] = True
        return True
