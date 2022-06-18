# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minCameraCover(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        def mon(node):
            if node.left is None and node.right is None:
                return 1,1,0
            if node.left is None:
                ri,rc,rp=mon(node.right)
                return min([ri,rp,rc])+1,ri,min(ri,rc)
            if node.right is None:
                li,lc,lp=mon(node.left)
                return min([li, lp, lc])+1, li, min(li, lc)
            li, lc, lp = mon(node.left)
            ri, rc, rp = mon(node.right)
            return min([li, lp, lc]) +  min([ri, rc, rp]) + 1, min(ri + min([li, lc]), li + min([ri, rc])), min(ri, rc) + min(li, lc)

        i,c,p = mon(root)
        return min([i, c, p+1])
            
        