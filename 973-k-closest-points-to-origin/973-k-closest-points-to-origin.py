class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda point: point[0] ** 2 + point[1] ** 2)  # if x <= y, sqrt(x) <= sqrt(y) -- so we don't have to apply sqrt for sorting
        return points[:k]