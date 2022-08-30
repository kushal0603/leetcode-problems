class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # first we transpose the matrix.
        for r in range(len(matrix)):
            for c in range(r):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        
		# after that we see if we reverse every row of the matrix, 
		# we get the answer.
        
        for r in matrix:
            r.reverse()