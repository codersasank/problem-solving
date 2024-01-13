class Solution:
    def repeatedRows(self, arr, m ,n):
        tuple_dict = dict()
        ret = list() ; idx = 0
        for row in arr:
            t_row = tuple(row)
            if t_row in tuple_dict:
                ret.append(idx)
            tuple_dict[t_row] = True
            idx += 1
        return ret
