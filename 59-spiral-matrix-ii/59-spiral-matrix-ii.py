class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        spiral = [[0 for _ in range(n)] for _ in range(n)]
        loop = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        loop_count, i, j = 0, 0, 0
        
        for v in range(1, n * n + 1):
          spiral[i][j] = v
          i, j = i + loop[loop_count % 4][0], j + loop[loop_count % 4][1]
          
          if i == n or j == n or spiral[i][j] != 0:
            i, j = i - loop[loop_count % 4][0], j - loop[loop_count % 4][1]
            loop_count += 1
            i, j = i + loop[loop_count % 4][0], j + loop[loop_count % 4][1]
          
        return spiral