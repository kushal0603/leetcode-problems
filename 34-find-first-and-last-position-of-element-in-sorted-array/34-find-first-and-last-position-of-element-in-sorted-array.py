class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [-1,-1] if nums.count(target) == 0 else [nums.index(target), len(nums)-1-nums[::-1].index(target)]