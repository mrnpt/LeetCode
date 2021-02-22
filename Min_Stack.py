class MinStack:
    stack = []
    init_pos = 0
    def __init__(self):
        self.init_pos = -1
        self.stack = []
    def push(self, x:int) -> None:
        self.init_pos += 1
        self.stack.append(x)
    def pop(self) -> None:
        del self.stack[-1]
    def top(self) -> int:
        return self.stack[-1]
    def getMin(self) -> int:
        return min(self.stack)

obj = MinStack()
obj.push(2)
obj.pop()
p3 = obj.top()
p4 = obj.getMin()
print(p3, p4)