class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        new=sorted(nums)
        n=len(nums)//2
        return new[n]