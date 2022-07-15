# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = cur = ListNode(0)
        add = 0
        while l1 or l2:
            val = (l1.val if l1 is not None else 0) + (l2.val if l2 is not None else 0) + add
            add = val // 10
            cur.next = ListNode(val % 10)
            cur = cur.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        if add:
            cur.next = ListNode(add)
        return ans.next
        