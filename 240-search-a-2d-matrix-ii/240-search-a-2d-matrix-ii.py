class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return any([target in matrix[i] for i in range(len(matrix))])
        