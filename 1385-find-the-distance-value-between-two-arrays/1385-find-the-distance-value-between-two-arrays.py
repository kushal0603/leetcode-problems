class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        cnt = 0
        for i in range(len(arr1)):
            l, r = 0, len(arr2) - 1
            while l <= r:
                m = l + (r - l) // 2
                if abs(arr1[i] - arr2[m]) <= d:
                    break
                elif arr2[m] < arr1[i]:
                    l = m + 1
                else:
                    r = m - 1
            cnt += l > r 
        return cnt