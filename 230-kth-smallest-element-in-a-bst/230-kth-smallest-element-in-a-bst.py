class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        f = lambda x: [x.val] + f(x.right) + f(x.left) if x else []        
        return sorted(f(root))[k-1]