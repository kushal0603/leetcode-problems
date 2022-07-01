class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return TreeNode(root.val, self.insertIntoBST(root.left, val) if root.val > val else root.left, self.insertIntoBST(root.right, val) if root.val < val else root.right) if root else TreeNode(val)