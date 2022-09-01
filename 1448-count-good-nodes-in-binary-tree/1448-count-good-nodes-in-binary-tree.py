class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        
        def rec(node, max_value):
            nonlocal ans
            if node is None:
                return
            if node.val >= max_value:
                ans += 1
            
            rec(node.left, max(max_value, node.val))
            rec(node.right, max(max_value, node.val))
        
        rec(root, -1e10)
        
        return ans