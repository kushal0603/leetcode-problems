class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a=[]
        t=0
        for i in nums:
            t+=i
            a.append(t)
        return a
        