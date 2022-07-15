class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()          # Sort the intervals
        ans = 0
        for ind in range(1, len(intervals)):
            if intervals[ind][0]<intervals[ind-1][1]:       # If previous interval ending is greater than current interval begining so we have got an interval to remove!
                ans += 1                
                if intervals[ind-1][1] <= intervals[ind][1]:   # If current interval ending is greater than or equal to previous interval ending then we replace current interval with previous interval.(i.e. we removed current interval)
                    intervals[ind] = intervals[ind-1]
        return ans