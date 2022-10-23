class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        diff = squared_diff = 0
        for i, num in enumerate(nums, 1):
            diff += i - num
            squared_diff += i * i - num * num
            
        sum_ = squared_diff // diff
        return [(sum_ - diff) // 2, (sum_ + diff) // 2]