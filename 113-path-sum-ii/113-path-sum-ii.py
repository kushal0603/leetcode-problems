class Solution:
    def pathSum(self, head: Optional[TreeNode], ts: int) -> List[List[int]]:
        ans=[]
        
        def trav(root, lst):
            if(not root):
                return
            
            if(root.left == None and root.right == None and root.val+sum(lst)==ts):
                lst.append(root.val)
                ans.append(lst)
            else:
                lst.append(root.val)
                trav(root.left, lst.copy())
                trav(root.right, lst.copy())
            
        trav(head, [])
        
        return ans