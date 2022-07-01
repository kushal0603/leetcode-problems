# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s = head
        while s:
            if s.next and s.val == s.next.val:
                s.val = s.next.val
                s.next = s.next.next
            else: s = s.next
        return head 