class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        idx = sorted(range(len(startTime)), key=startTime.__getitem__)
        startTime = [startTime[i] for i in idx]
        endTime = [endTime[i] for i in idx]
        profit = [profit[i] for i in idx]
        dp = [0 for _ in range(len(idx))]
        dp[-1] = profit[-1]
        
        def find_index(low, high, target):
            if low > high:
                return low
            mid = (low + high) //2
            if startTime[mid] >= target:
                return find_index(low, mid-1, target)
            return find_index(mid+1, high, target)
                
        for i in range(len(idx)-2, -1, -1):
            # find the index of the first job starting
            # after ith job has finished
            # to find that, we find the element which is 
            # equal to or next greater than endTime[i] in startTime
            index = find_index(i, len(startTime)-1, endTime[i])
            res = dp[index] if index < len(startTime) else 0
            dp[i] = max(profit[i] + res, dp[i+1])
        return dp[0]