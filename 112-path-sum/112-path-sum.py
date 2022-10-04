class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.exist = False
        def traverse(node, curSum):
            if node is not None:
                curSum += node.val
                if not node.left and not node.right:
                    if curSum == targetSum:
                        self.exist = True
                else:
                    traverse(node.left, curSum)
                    traverse(node.right, curSum)
                curSum -= node.val
        traverse(root, 0)
        return self.exist