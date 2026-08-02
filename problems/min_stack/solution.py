class MinStack:

    def __init__(self):
        self.cont = []        

    def push(self, value: int) -> None:
        min_val = self.getMin()
        if min_val == None or value < min_val:
            min_val = value
        self.cont.append((value, min_val))
        

    def pop(self) -> None:
        self.cont.pop()
        

    def top(self) -> int:
        return self.cont[-1][0] if self.cont else None
        

    def getMin(self) -> int:
        return self.cont[-1][1] if self.cont else None
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()