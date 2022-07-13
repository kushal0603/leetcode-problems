class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return None
        queue = [root]
        while queue:
            prev_node = None
            for i in range(len(queue)):
                node = queue.pop(0)
                if prev_node is not None:
                    prev_node.next = node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                prev_node = node
            prev_node.next = None

        return root