class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        if(len(nums) == 1):
            return nums[0]
        
        nums = sorted(nums)
        start = 0
        end = 2
        while(end <= len(nums)-1):
            curr_split = nums[start : end]
            if(curr_split[0] != curr_split[1]):
                return curr_split[0]
            start = start +2
            end = end +2
        return nums[len(nums)-1]