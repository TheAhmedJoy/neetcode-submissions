class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1

        while top <= bottom:
            middle_row = top + ((bottom - top) // 2)

            if matrix[middle_row][-1] < target:
                top = middle_row + 1
            elif matrix[middle_row][0] > target:
                bottom = middle_row - 1
            else:
                break
        
        if not (top <= bottom):
            return False

        left = 0
        right = len(matrix[0]) - 1 
        middle_row = top + ((bottom - top) // 2)

        while left <= right:
            middle_col = left + ((right - left) // 2)

            if matrix[middle_row][middle_col] < target:
                left = middle_col + 1
            elif matrix[middle_row][middle_col] > target:
                right = middle_col - 1
            else:
                return True
        
        return False