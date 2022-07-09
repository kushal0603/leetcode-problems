class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tempHead = ListNode(-1, head)
        slow = tempHead
        fast = tempHead
        while fast.next:
            if not n:
                slow = slow.next
            else:
                n-=1
            fast = fast.next
        print(slow.val, fast.val)
        slow.next = slow.next.next
        return tempHead.next