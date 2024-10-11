class Solution:
    def rearrange(self, arr):
        n = len(arr)
        if -1 not in arr:
            for i in range(n):
                arr[i] = i
            return arr
        for i in range(n):
            print ("Start", i, arr[i])
            temp = arr[i]
            if temp==i or temp==-1:
                continue
            while arr[i]!=-1 and arr[i]!=i:
                if arr[i]==arr[arr[i]]:
                    arr[i] = -1
                    break
                print ( arr[i] , arr[arr[i]])
                temp = arr[arr[i]]
                arr[arr[i]] = arr[i]
                arr[i] = temp
                #arr[i], arr[arr[i]] = arr[arr[i]], arr[i]
        return arr
