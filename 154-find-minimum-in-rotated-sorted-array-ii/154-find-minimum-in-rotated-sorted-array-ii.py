class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n-1
        while(left +1 <right):
            mid = left + (right-left)//2
            if (nums[mid] > nums[right]):
                left +=1
            else:
                right -=1
        return min(nums[left], nums[right])