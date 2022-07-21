class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        
        def dfs(root, sol, cur):
            if root == None:
                return 
            
            cur = cur + root.val
            
            if cur == targetSum and not root.left and not root.right:
                res.append(sol+[root.val])
                
            dfs(root.left, sol+[root.val], cur)
            dfs(root.right, sol+[root.val], cur)
            
        dfs(root, [], 0)
        return res