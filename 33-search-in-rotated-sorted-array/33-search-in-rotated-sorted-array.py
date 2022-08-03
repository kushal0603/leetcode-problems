class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def find_target(low, high):
            while low <= high:
                mid = low + (high - low) // 2
                if nums[mid] < target:
                    low = mid + 1
                elif nums[mid] > target:
                    high = mid - 1
                else:
                    return mid
            
            return -1
        
        N = len(nums)
        low = 0
        high = N - 1
        
        # FYI: low should be storing the index of the smallest
        # element after we complete the while-loop.
        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        
        # verifies whether target exists in the first list
        target_idx = find_target(0, low - 1)
        if target_idx != -1: return target_idx
        
        # verifies whether target exists in the second list
        target_idx = find_target(low, N - 1)
        if target_idx != -1: return target_idx
        
        return -1