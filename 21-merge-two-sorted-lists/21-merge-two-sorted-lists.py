class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        result_head = result
        
        while list1 and list2:
            if list2.val > list1.val:
                result.next = list1
                list1 = list1.next
            else:
                result.next = list2
                list2 = list2.next
                
            result = result.next
        
        result.next = list1 or list2
        return result_head.next