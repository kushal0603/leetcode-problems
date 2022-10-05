class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        result = root
		# 1. Recursive until depth is 1 or 0
        def dfs(root: Optional[TreeNode], val: int, depth: int):
            if root == None: return
            else:
				# 2. If depth is 1, replace left and right nodes by the new tree node with value
				#    and concat the old node after the new one following the previous direction
                if depth == 1:
                    newLeftNode = TreeNode(val, root.left, None)
                    root.left = newLeftNode
                    newRightNode = TreeNode(val, None, root.right)
                    root.right = newRightNode
				# 3. If depth is 0, replace root node by new tree node with the value
				#    and set root node to the left of the new node.
                elif depth == 0:
                    nonlocal result
                    newRootNode = TreeNode(val, root, None)
                    result = newRootNode
                else:
                    dfs(root.left, val, depth - 1)
                    dfs(root.right, val, depth - 1)
        dfs(root, val, depth - 1)
        return result