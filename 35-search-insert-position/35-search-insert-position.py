class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
		
        while i < len(nums):
            if nums[i] >= target : return i
            elif (( i + 1 < len(nums) and nums[i+1] > target ) or i + 1 == len(nums)) : return i + 1
            else : 
                i += 1