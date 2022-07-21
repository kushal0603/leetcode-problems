class Solution(object):
    def deleteNode(self, root, key):
        def findMin(root):
            if root is None:
                return None
            elif root.left is not None:
                return findMin(root.left)
            else:
                return root.val

        def findMax(root):
            if root is None:
                return None
            elif root.right is not None:
                return findMax(root.right)
            else:
                return root.val

        if root is None:
            return None

        if key == root.val:
            if root.right is not None:
                new_val = findMin(root.right)
                return TreeNode(new_val, root.left, self.deleteNode(root.right, new_val))
            elif root.left is not None:
                new_val = findMax(root.left)
                return TreeNode(new_val, self.deleteNode(root.left, new_val), root.right)
            else:
                return None
        elif key < root.val:
            return TreeNode(root.val, self.deleteNode(root.left, key), root.right)
        else:
            return TreeNode(root.val, root.left, self.deleteNode(root.right, key))