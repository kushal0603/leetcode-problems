from sortedcontainers import SortedList
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n=len(nums)
        arr=SortedList()
        ans=[]
        for num in nums[::-1]:
            idx=arr.bisect_left(num)
            ans.append(idx)
            arr.add(num)
        return ans[::-1]