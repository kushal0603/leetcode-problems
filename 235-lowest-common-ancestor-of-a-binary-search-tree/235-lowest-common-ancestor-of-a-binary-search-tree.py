class Solution:
    def traverse(self,node,p,q):
        if node:
            if p==node or q==node:return node
            if p.val<node.val and q.val>node.val:return node
            if p.val>node.val:return self.traverse(node.right,p,q)
            return self.traverse(node.left,p,q)
    def lowestCommonAncestor(self, root, p,q):
            if p.val>q.val:p,q=q,p
            return self.traverse(root,p,q)