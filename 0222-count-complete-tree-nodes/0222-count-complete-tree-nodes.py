class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q=deque()
        q.append(root)
        ans=0
        while q:
            head=q.popleft()
            ans+=1
            if head.left:
                q.append(head.left)
            if head.right:
                q.append(head.right)
        return ans