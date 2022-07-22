# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
	    a, b = ListNode(0, head), ListNode(0)
	    ap, bp = a, b
	    while ap.next:
		    if ap.next.val >= x: bp.next, bp, ap.next, bp.next = ap.next, ap.next, ap.next.next, None
		    else: ap = ap.next
	    ap.next = b.next
	    return a.next