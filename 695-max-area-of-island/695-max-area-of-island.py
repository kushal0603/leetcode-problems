class Solution:
    
    def __init__(self):
        self.directions = [(-1, 0),(1, 0),(0, -1),(0, 1)]
        
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == 1:
                    area = self.countSize(grid, i, j)
                    maxArea = max(area, maxArea)
        return maxArea
    
    def countSize(self, grid, row, col):
        if row not in range(0, len(grid)) or col not in range(0, len(grid[0])):
            return 0
        if grid[row][col] == 0:
            return 0
        
        grid[row][col] = 0
        
        size = 1
        for dr, dc in self.directions:
            size += self.countSize(grid, row + dr, col + dc)
        return size