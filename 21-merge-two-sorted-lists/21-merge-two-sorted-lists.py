class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()
        cur_node = dummy_head
        while list1 or list2:
            if (list1 and list2 and list1.val < list2.val) or (list1 and not list2):
                cur_node.next = list1
                list1 = list1.next
            else:
                cur_node.next = list2
                list2 = list2.next
            cur_node = cur_node.next
            cur_node.next = None
        return dummy_head.next