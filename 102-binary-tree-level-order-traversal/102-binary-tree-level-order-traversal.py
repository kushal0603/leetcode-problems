class Solution:
    def levelOrder(self, R: TreeNode) -> List[List[int]]:
        if R == None: return []
        A, V, C = [], [R.val], [R]
        while V:
            NV, C, V, _ = C, [], [], A.append(V)
            [[(V.append(x.val),C.append(x)) for x in [n.left,n.right] if x != None] for n in NV]
        return A