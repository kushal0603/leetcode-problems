class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if root is None:
            return None
        cur = TreeNode(root.val)
        cur.left = self.invertTree(root.right)
        cur.right = self.invertTree(root.left)

        return cur