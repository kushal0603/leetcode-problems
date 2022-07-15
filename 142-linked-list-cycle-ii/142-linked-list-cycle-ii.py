class Solution(object):
    def detectCycle(self, head):
        NodeSet=set();
        while(head!=None):
            NodeSet.add(head)
            head=head.next
            if head in NodeSet:
                return head;
        return None; 