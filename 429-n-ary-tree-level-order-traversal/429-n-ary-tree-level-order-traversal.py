

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []                        # Keep track of result
        
        def dfs(node, level):           # Helper function to traverse tree
            if not node:                # Base case is if node is null
                return
            
            if len(res) < level + 1:    # Add nested array to enable level-indexing
                res.append([])
            res[level].append(node.val) # Append node value to current level (0-indexed)
            
            for child in node.children: # Traverse down to each children, to the next level
                dfs(child, level + 1)
        
        dfs(root, 0)                    # Initiate the traversal on the root at level 0
        return res                      # Return the final result