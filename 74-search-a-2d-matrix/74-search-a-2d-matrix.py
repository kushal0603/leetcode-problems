class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        
        for i in range(ROWS-1, -1,-1):
            if matrix[i][0] == target:
                return True
            elif matrix[i][0] > target:
                continue
            else:
                for j in range(COLS):
                    if matrix[i][j] == target:
                        return True
        
        return False