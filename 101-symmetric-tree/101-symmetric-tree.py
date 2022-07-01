class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.mirror(root, root)
    
    def mirror(self, t1, t2):
        if t1 is None and t2 is None:
            return True
        if t1 is None or t2 is None:
            return False
        return(t1.val == t2.val) and self.mirror(t1.right, t2.left) and self.mirror(t1.left, t2.right)