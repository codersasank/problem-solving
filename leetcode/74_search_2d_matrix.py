class Solution:
    def bsearch(self, arr, left, right, target):
        if (left > right):
            return False
        mid = (left + right)//2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            return self.bsearch(arr, mid+1, right, target)
        else:
            return self.bsearch(arr, left, mid-1, target)
    def find_row(self, matrix, left, right, target):
        if left > right:
            return False
        n = len(matrix[0])
        mid = (left+right)//2
        if matrix[mid][0] == target:
            return True
        elif matrix[mid][0] < target:
            if mid == len(matrix) - 1:
                return self.bsearch(matrix[mid], 0, n-1, target)
            elif matrix[mid+1][0] < target:
                return self.find_row(matrix, mid+1, right, target)
            elif matrix[mid+1][0] > target:
                return self.bsearch(matrix[mid], 0, n-1, target)
            else:
                return True
        elif matrix[mid][0] > target:
            if mid == 0:
                return False
            elif matrix[mid-1][0] < target:
                return self.bsearch(matrix[mid-1], 0, n-1, target)
            elif matrix[mid-1][0] > target:
                return self.find_row(matrix, left, mid-1, target)
            else:
                return True
        
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix)==1:
            return self.bsearch(matrix[0], 0, len(matrix[0])-1, target)
        return self.find_row(matrix, 0, len(matrix)-1, target)

