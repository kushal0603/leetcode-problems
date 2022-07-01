class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return [root.val]+self.preorderTraversal(root.left)+self.preorderTraversal(root.right) if root else []