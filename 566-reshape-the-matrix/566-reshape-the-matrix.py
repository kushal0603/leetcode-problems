import numpy as np
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
         if r * c == len(mat) * len(mat[0]):
            return np.reshape(mat,(r, c))
         else:
            return mat       