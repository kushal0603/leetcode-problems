class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # early termination
        if not root:
            return 0
        
        # function to find sum counts for a given starting node using DFS
        def dfs(root, tgt):
            count = 0
            if root is None:
                return count
            if root.val == tgt:
                count += 1
            if root.left is not None:
                count += dfs(root.left, tgt-root.val)
            if root.right is not None:
                count += dfs(root.right, tgt-root.val)
            return count
        
        # using BFS, get count of paths summing to total for each starting node
        total_count, q = 0, [root]
        while q:
            for node in q:
                total_count += dfs(node, targetSum)
            q = [child for node in q for child in (node.left, node.right) if child is not None]
        
        return total_count