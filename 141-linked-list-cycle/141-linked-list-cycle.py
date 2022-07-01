class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        while head:
            if head.val == "Already Passed":
                return True
            head.val = "Already Passed"
            head = head.next
        return False