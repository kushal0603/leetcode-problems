class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        c=0
        t=head
        if head.next is None:
            return None
        while(t is not None):
            c+=1
            t=t.next
        x=c//2
        i=0
        temp=head
        while(i<x-1):
            temp=temp.next
            i+=1
        print(temp.val)
        temp.next=temp.next.next
        
        return head