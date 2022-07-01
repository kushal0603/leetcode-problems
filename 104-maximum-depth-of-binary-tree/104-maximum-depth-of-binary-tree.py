class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        self.answer = 0; depth = 1
        
        def maximumDepth(root, depth):
            
            if not root:
                return
            else:
                if not root.right and not root.left:
                    self.answer = max(self.answer, depth)
                    
                maximumDepth(root.left, depth + 1)
                maximumDepth(root.right, depth + 1)
        
        maximumDepth(root, depth)
        
        return self.answer