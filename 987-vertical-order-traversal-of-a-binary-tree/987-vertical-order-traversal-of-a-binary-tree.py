class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = defaultdict(lambda: defaultdict(list))
        
        def extract(node, row, col):
            if node is None: return
            d[col][row].append(node.val)
            extract(node.left, row+1, col-1)
            extract(node.right, row+1, col+1)
            return
        
        extract(root, 0, 0)
        
        ans = []
        
        for col in sorted(list(d.keys())):
            rows = d[col]
            temp = []
            for r in sorted(list(rows.keys())):
                row = rows[r]
                temp += sorted(row)
            ans.append(temp)
            
        return ans