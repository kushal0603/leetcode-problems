class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.stack = []
        self.push(root)
    
    def push(self,root):
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        res = self.stack.pop()
        self.push(res.right)
        return res.val
        

    def hasNext(self) -> bool:
        return len(self.stack)