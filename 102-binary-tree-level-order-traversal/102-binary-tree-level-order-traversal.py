from collections import deque

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = deque()
        traversal = []
        
        if not root:
            return traversal
        
        queue.append(root)
        
        while queue:
            level = []
            level_size = len(queue)
            
            for _ in range(level_size):
                item = queue.popleft()
                level.append(item.val)
                
                if item.left:
                    queue.append(item.left)
                
                if item.right:
                    queue.append(item.right)
        
            traversal.append(level)
        
        return traversal