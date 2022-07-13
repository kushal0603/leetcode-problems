class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        return len([i for lt in grid for i in lt if i < 0])
        