class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while p and q and (root.val-p.val)*(root.val-q.val)>0:
            if root.val>p.val:
                root = root.left
            else:
                root = root.right
        return root