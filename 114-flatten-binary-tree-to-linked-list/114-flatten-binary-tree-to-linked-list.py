class Solution:
    pre=None    
    def flatten(self, root):
        if root:
            self.flatten(root.right)
            self.flatten(root.left)
            root.right= self.pre
            root.left = None
            self.pre  = root