class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        l, r = map(lambda x: x and self.lowestCommonAncestor(x, p, q), (root.left, root.right))
        return (root in (p, q) or l and r) and root or l or r