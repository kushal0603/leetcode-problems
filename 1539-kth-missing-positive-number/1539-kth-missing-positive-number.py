class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        for i, num in enumerate(arr+[9999]):
            if num - (i+1) >= k:
                return k + i