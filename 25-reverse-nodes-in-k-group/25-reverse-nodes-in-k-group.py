class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        count, node = 1, head
        while node and count < k:
            node = node.next
            count += 1
        if not node:
            return head

        node.next = self.reverseKGroup(node.next, k)
        p, q = head, head.next
        while head != node:
            p.next = q.next
            q.next = head
            head, q = q, p.next
        return head