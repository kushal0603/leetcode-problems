class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head is not None and head.val == val:
            head = head.next
        p = head
        q = head
        while p is not None:
            if p.val == val:
                p = p.next
                q.next = p
            else:
                q = p
                p = p.next
        return head