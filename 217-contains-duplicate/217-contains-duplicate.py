class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        log = dict()
        for num in nums:
            if  num in log:
                 return True
            else:
                 log[num] = 100
        