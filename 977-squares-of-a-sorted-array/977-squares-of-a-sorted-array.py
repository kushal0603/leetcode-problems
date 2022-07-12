class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        i, j = 0, len(nums)-1
        
        res = [None] * (j + 1)
        
        for r in range(j, -1, -1):
            if abs(nums[i]) > abs(nums[j]):
                res[r] = nums[i] ** 2
                i += 1
                
            else:
                res[r] = nums[j] ** 2
                j -= 1
        else:
            return res