# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head):
        dummy=prev=ListNode(0)
        prev.next=head
        while head and head.next:
            head.next.next,head.next,prev.next,prev,head=head,head.next.next,head.next,head,head.next.next
        return dummy.next