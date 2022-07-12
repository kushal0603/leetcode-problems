class Solution:
    #def twoSum(self, numbers: List[int], target: int) -> List[int]:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        while left < right:
            total = nums[left] + nums[right]
            if total > target:
                right -= 1
            elif total < target:
                left += 1
            else:
                return [left + 1, right + 1]
        return []
        