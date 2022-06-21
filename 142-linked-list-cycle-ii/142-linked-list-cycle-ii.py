# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        
        slow, fast = head, head.next
        while fast and fast.next and fast != slow:
            slow = slow.next
            fast = fast.next.next
        
        
        if fast is None or fast.next is None:
            return None
        
        node, pos = head, 0
        
        if node == slow:
            return node
        
        slow = slow.next
        while node != slow:
            while slow != fast:
                if slow == node:
                    return node
                slow = slow.next
            slow = slow.next
            pos += 1
            node = node.next
        return node