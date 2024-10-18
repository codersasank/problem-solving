class Solution:
    def zigZag(self, n : int, arr : List[int]) -> None:
        for i in range(1,n,2):
            if i+1!=n:
                arr[i-1], arr[i], arr[i+1] = sorted([arr[i-1], arr[i], arr[i+1] ])
                arr[i], arr[i+1] = arr[i+1], arr[i]
            else:
                arr[i-1], arr[i] = sorted([arr[i-1], arr[i] ])
