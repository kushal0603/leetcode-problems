class MinStack:

    def __init__(self):
        self.arr = []
    

    def push(self, x: int) -> None:
        self.arr.append(x)
    

    def pop(self) -> None:
        self.arr.pop()
    

    def top(self) -> int:
        return self.arr[-1]
    

    def getMin(self) -> int:
        return min(self.arr)