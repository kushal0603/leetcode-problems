class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum_ = l = 0
        min_ = float('inf')
        for r in range(len(nums)):
            sum_ += nums[r]
            while sum_ >= target:
                min_ = min(min_, r-l+1)
                sum_ -= nums[l]
                l += 1
        return min_ if min_ != float('inf') else 0