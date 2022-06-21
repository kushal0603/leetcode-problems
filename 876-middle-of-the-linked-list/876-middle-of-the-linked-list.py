# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = [] 
        while head: 
            nodes.append(head) # push each node in list
            head = head.next # keep moving
        return nodes[(len(nodes))//2] 