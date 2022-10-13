class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val=node.next.val # setting node value to value of next node 
		
        node.next=node.next.next # setting node pointer to point what next node is pointing
		