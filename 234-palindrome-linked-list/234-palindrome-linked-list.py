class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        a = ''
        while head != None:
            a += str(head.val)
            head = head.next
        if a == a[::-1]:
            return True
        else:
            return False