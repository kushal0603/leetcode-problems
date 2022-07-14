class Solution:
    def buildTree(self, P: List[int], I: List[int]) -> Optional[TreeNode]:
        if not I:return None
        val=P.pop(0)
        i=I.index(val)
        return TreeNode(val,self.buildTree(P,I[:i]),self.buildTree(P,I[i+1:]))