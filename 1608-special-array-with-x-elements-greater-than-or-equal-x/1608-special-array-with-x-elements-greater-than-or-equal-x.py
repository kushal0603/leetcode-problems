class Solution:
    def specialArray(self, nums: List[int]) -> int:
        return next((i for i in range(0, max(nums)+1) if sum(j>=i for j in nums)==i), -1)