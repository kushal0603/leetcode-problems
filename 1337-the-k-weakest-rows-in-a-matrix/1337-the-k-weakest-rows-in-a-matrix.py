class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return list(map(lambda x: x[1], heapq.nsmallest(k, [(row.count(1), idx) for idx, row in enumerate(mat)])))