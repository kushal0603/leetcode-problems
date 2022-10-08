class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = float('inf')
        for i in range(len(nums) - 2):
            lo, hi = i + 1, len(nums) - 1
            
            while lo < hi:
                s = nums[i] + nums[lo] + nums[hi]
                if s == target:
                    return s
                elif s > target:
                    hi -= 1
                else:
                    lo += 1
                if abs(s - target) < abs(ans - target):
                    ans = s
        return ans