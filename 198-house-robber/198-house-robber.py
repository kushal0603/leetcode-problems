class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        else:
            second = nums[0]
            first = max(nums[0], nums[1])
            
            for i in range(2,len(nums)):
                current = max(first, second + nums[i])
                second = first
                first = current
                
            return first