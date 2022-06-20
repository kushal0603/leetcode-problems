class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_local = max_global = nums[0]
        for n in nums[1:]:
            max_local = max(max_local + n, n)
            max_global = max(max_global, max_local)
        return max_global
        