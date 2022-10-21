class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic  = {}
        _len = len(nums)
        
        for i in range(_len):
            n = nums[i]
			
            if n in dic:
                if i - dic[n] <= k:
                    return True
            dic[n] = i
			
        return False