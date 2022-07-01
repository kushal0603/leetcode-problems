class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        s = set()
        def dfs(n):
            return n and any((dfs(n.left), dfs(n.right), n.val in s, s.add(k-n.val)))
        return dfs(root)