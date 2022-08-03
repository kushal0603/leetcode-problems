class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if sum(nums) %2 != 0:
            return False
        target = sum(nums) // 2
        cache = {}
        
        def dfs(nums, target):
            if target == 0:
                return True
            if target in cache:
                return cache[target]
            for i in range(len(nums)):
                if nums[i] <= target and dfs(nums[:i] + nums[i +1:], target - nums[i]):
                    return True
            cache[target] = False
            return False
            
        return dfs(nums,target)