class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        array = []
        
        def helper(array,tree):
            if tree is None:
                return
            helper(array,tree.left)
            if len(array) == k:
                return
            else:
                array.append(tree.val)
            helper(array,tree.right)
        
        helper(array,root)
        
        return array[len(array)-1]