class Solution:
    def firstBadVersion(self, n):
        result = self.divideSearch((n+1)//2, 1, n)
        return result

    def divideSearch(self, current, start, end):
        if isBadVersion(current):
            if current==start:
                return start
            elif not isBadVersion(current-1):
                return current
            else:
                return self.divideSearch((start+current)//2, start, current)
        else:
            return self.divideSearch((current+end)//2+1, current+1, end)