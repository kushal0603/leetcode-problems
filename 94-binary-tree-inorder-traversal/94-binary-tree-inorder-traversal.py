class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        self.traverse(root, result)
        
        return result
    
    def traverse(self, root: Optional[TreeNode], result: List[int]):
        if root:
            self.traverse(root.left, result)
            
            result.append(root.val)
            
            self.traverse(root.right, result)