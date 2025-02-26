class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if n == 0:
            return
        ptr1 = n
        ptr2 = 0
        for i in range(m+n-1, n-1, -1):
            nums1[i] = nums1[i-n]
        i = 0
        while ptr1 < m+n and ptr2 < n:
            if nums1[ptr1] <= nums2[ptr2]:
                nums1[i] = nums1[ptr1]
                ptr1 += 1
            else:
                nums1[i] = nums2[ptr2]
                ptr2 += 1
            i += 1
        if ptr1 == m+n and ptr2 != n:
            for j in range(i, m+n):
                nums1[j] = nums2[ptr2+j-i]
        
