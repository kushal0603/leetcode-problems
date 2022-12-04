class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        rsu = sum(nums)
        n = len(nums)
        mindiff = sys.maxsize
        res = -1
        lsu = 0
        for i in range(n-1):
            rsu -= nums[i]
            lsu += nums[i]
            d = abs(lsu//(i+1) - rsu//(n-i-1))
            if d < mindiff:
                res = i
                mindiff = d

        d = abs((lsu+nums[-1])//n)
        if d< mindiff:
            res = n-1
            mindiff = d
        return res