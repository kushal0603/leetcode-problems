class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        queue = [root]
        
        output = []
        while queue:
            
            level = []
            
            for i in range(len(queue)):
                level.append(queue.pop(0))
            
            if level:
                output.append([i.val for i in level])
                
                for j in level:
                    if j.left:
                        queue.append(j.left)
                    if j.right:
                        queue.append(j.right)

        return output