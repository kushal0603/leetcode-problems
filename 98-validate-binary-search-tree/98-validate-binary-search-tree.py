class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root, low, high):
            if root is None:
                return True
            
            if root.val <= low or root.val >= high:
                return False
            
            return helper(root.left, low, root.val) and helper(root.right, root.val, high)
        
        return helper(root, -math.inf, math.inf)