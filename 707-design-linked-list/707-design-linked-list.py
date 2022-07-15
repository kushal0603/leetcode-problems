class MyLinkedList:

    def __init__(self):
        self.llist = {}

    def get(self, index: int) -> int:
        if(self.llist.get(index) == None):
            return -1
        return self.llist.get(index)

    def addAtHead(self, val: int) -> None:
        llist = self.llist
        for i in reversed(range(len(llist))):
            llist[i+1] = llist.get(i)
        llist[0] = val

    def addAtTail(self, val: int) -> None:
        self.llist[len(self.llist)] = val

    def addAtIndex(self, index: int, val: int) -> None:
        llist = self.llist        
        if(index<=len(llist)):
            for i in reversed(range(index,len(llist))):
                llist[i+1] = llist.get(i)
            llist[index] = val

    def deleteAtIndex(self, index: int) -> None:
        llist = self.llist
        if(index<len(llist)):
            for i in range(index,len(llist)-1):
                llist[i] = llist.get(i+1)
            del llist[len(llist)-1]