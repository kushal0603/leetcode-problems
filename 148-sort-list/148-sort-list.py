class Solution:
    def split(self, head):
        prev = None
        slow = fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        if prev: prev.next = None
        return slow
    
    def merge(self, l1, l2):
        dummy = tail = ListNode()
        while l1 or l2:
            v1 = l1.val if l1 else inf
            v2 = l2.val if l2 else inf
            if v1 <= v2:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        return dummy.next
            
    
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        head2 = self.split(head)
        
        head1 = self.sortList(head)
        head2 = self.sortList(head2)
        
        return self.merge(head1, head2)