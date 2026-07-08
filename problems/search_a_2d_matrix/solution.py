class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_top = 0 # pointer from top row down 
        row_bot = len(matrix) # pointer from bottom row up 
        row_final = row_top
        while row_top < row_bot:
            mid = row_top + (row_bot - row_top) // 2
            if matrix[mid][0] < target:
                row_top = mid + 1
            elif matrix[mid][0] > target:
                row_bot = mid 
            else: 
                return True
            
        row_final = row_top - 1
        left = 0
        right = len(matrix[0])
        while left < right:
            mid2 = left + (right - left) // 2 
            if matrix[row_final][mid2] < target:
                left = mid2 + 1
            elif matrix[row_final][mid2] > target:
                right = mid2 
            else: 
                return True
        return False
