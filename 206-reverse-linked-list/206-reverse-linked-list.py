class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = None
        elements = []
        
        while head:
            elements.append(head.val)
            head = head.next
        
        for iterator in elements:
            newNode = ListNode(iterator)
            newNode.next = curr
            curr = newNode
            
        return curr