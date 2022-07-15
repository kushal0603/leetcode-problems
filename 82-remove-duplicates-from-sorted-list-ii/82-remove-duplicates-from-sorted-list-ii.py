class Solution(object):
    def deleteDuplicates(self, head):
        result = tail = ListNode(None)
        while head:
            while head.next and head.val == head.next.val:
                head = head.next
                if not head.next or head.val != head.next.val:
                    break
            else:
                tail.next, tail = head, head
            head = head.next
        tail.next = None
        return result.next
