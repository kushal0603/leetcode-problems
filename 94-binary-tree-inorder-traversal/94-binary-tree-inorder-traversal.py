class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []
        if root == None:
            return res
        
        res += self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        
        return res