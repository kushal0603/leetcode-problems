class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return None if len(nums) == 0 else TreeNode(nums[0]) if len(nums) == 1 else TreeNode(nums[len(nums)//2], self.sortedArrayToBST(nums[:len(nums)//2]), self.sortedArrayToBST(nums[len(nums)//2+1:]))