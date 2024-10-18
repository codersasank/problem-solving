class Solution:
    def common_element(self,v1,v2):
        freq1 = dict()
        freq2 = dict()
        ret = list()
        for num in v1:
            freq1[num] = freq1.get(num, 0) + 1
        for num in v2:
            freq2[num] = freq2.get(num, 0) + 1
        list_freq1 = [num for num in freq1]
        list_freq1.sort()
        for num in list_freq1:
            if num not in freq2:
                continue
            cnt = min ( freq1[num], freq2[num])
            for i in range(cnt):
                ret.append(num)
        return ret
