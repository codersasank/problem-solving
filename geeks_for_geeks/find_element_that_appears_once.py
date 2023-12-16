class Solution:
    def findOnce(self,arr : list, n : int):
        if n==1:
            return arr[0]
        left = 0 ; right = n-1 ; mid = (left+right)//2
        while left<=right:
            mid = (left+right)//2
            if mid%2==0:
                if mid==n-1:
                    if arr[mid-1]!=arr[mid]:
                        return arr[mid]
                    else:
                        right = mid-2
                elif arr[mid+1]==arr[mid]:
                    left = mid+2
                elif mid==0 or arr[mid-1]!=arr[mid]:
                    return arr[mid]
                else:
                    right = mid-2
            else:
                if arr[mid-1]==arr[mid]:
                    left = mid+1
                elif mid==n-1 or arr[mid+1]!=arr[mid]:
                    return arr[mid]
                else:
                    right = mid-1
                    
