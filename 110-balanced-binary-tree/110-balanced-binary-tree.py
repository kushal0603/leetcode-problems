class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def get_height(root: Optional[TreeNode]):
            if not root:
                return 0
            else:
                h1 = get_height(root.left)
                h2 = get_height(root.right)
                if abs(h1 - h2) > 1:
                    raise ValueError('Unbalanced tree')
                return max(h2, h1) + 1
        
        try:
            get_height(root)
        except ValueError:
            return False
        else:
            return True