class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        @cache
        def dfs(i: int, j: int, moves: int) -> int:
            if moves < 0: return 0
            if i < 0 or j < 0 or i >= m or j >= n: return 1
            return sum(dfs(r, c, moves - 1) for r, c in [(i-1, j), (i+1,j), (i,j-1), (i,j+1)])
        return dfs(startRow, startColumn, maxMove) % (10**9 + 7)