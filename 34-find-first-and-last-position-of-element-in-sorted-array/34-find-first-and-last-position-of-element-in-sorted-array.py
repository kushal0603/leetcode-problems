class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l=[]
        for i in range(len(nums)):
            if(nums[i]==target):
                l.append(i)
        if(len(l)==0):
            return [-1,-1]
        else:
            m=[]
            m.append(min(l))
            m.append(max(l))
            return m