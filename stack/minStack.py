class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        min_val = self.getMin()
        if min_val == None or val < min_val:
            min_val = val

        self.stack.append((val, min_val))

    def pop(self) -> None:
        self.stack.pop()[0]

    def top(self) -> int:
        return self.stack[-1][0] if len(self.stack) > 0 else None

    def getMin(self) -> int:
        return self.stack[-1][1] if len(self.stack) > 0 else None


obj = MinStack()
obj.push(-3)
obj.push(0)
obj.push(-2)
# print(obj.getMin())

obj.pop()
obj.push(-9)
print(obj.getMin())
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
