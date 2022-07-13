class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def preorder(root1, root2):
            if root1 == None and root2 == None:
                return None
            
            if root1 == None:
                return root2
            elif root2 == None:
                return root1
            else:
                root = TreeNode(root1.val+root2.val)

                root.left =  preorder(root1.left, root2.left)
                root.right = preorder(root1.right, root2.right)
                return root
            
        return preorder(root1, root2)