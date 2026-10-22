class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0 
        bot = len(matrix) - 1

        while top <= bot: 
            row = top + ((bot - top) // 2)

            if target > matrix[row][-1]:
                top = row + 1 
            elif target < matrix[row][0]:
                bot = row - 1
            else: 
                break 

        if not (top <= bot):
            return False 

        row = top + (bot - top) // 2 

        left = 0 
        right = len(matrix[row]) - 1

        while left <= right: 
            mid = (left + (right - left) // 2)
            if target < matrix[row][mid]:
                right = mid - 1
            elif target > matrix[row][mid]:
                left = mid + 1
            else: 
                return True 
        return False
