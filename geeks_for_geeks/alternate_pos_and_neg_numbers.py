class Solution:
    def rearrange(self,arr):
        pos = neg = 0
        new_arr = list()
        n = len(arr)
        pos_turn = True
        while pos<n or neg<n:
            print ( pos , neg, pos_turn )
            if pos_turn:
                while pos<n and arr[pos]<0:
                    pos += 1
                if pos==n:
                    pos_turn = not(pos_turn)
                    continue
                new_arr.append(arr[pos])
                pos += 1
            else:
                while neg<n and arr[neg]>=0:
                    neg += 1
                if neg==n:
                    pos_turn = not(pos_turn)
                    continue
                new_arr.append(arr[neg])
                neg += 1
            pos_turn = not(pos_turn)         
        arr.clear()
        arr += new_arr
