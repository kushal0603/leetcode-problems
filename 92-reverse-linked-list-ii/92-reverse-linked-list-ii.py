class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummy = node = ListNode(next=head)
        prev = None
        for _ in range(left): node, prev = node.next, node 
        pp, nn = prev, node 
        
        for _ in range(left, right+1): node.next, node, prev = prev, node.next, node 
        pp.next, nn.next = prev, node
        
        return dummy.next 