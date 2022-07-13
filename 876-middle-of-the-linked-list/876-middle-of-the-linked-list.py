class Solution(object):
    def middleNode(self, head):
        fast, slow = head, head
        while slow.next and fast.next:
            slow = slow.next
            fast = fast.next
            if not fast.next:
                return slow
            fast = fast.next
        return slow