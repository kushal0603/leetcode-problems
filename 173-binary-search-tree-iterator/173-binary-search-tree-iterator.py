class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.aux = self.inorderTraversal(root)
        
    def inorderTraversal(self, node):
        aux = []
        if not node:
                return None
        else:
            if node.left:
                aux += self.inorderTraversal(node.left)
            aux += [node.val]
            if node.right:
                aux += self.inorderTraversal(node.right)
        return aux             
        
    def next(self) -> int:
        return self.aux.pop(0)

    def hasNext(self) -> bool:
        if self.aux:
            return True
        else:
            return False