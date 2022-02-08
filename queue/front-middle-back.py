class FrontMiddleBackQueue:

    def __init__(self):

        self.queue = []

    def pushFront(self, val: int) -> None:

        self.queue.insert(0, val)

    def pushMiddle(self, val: int) -> None:

        middle_index = len(self.queue)//2

        self.queue.insert(middle_index, val)

    def pushBack(self, val: int) -> None:

        self.queue.append(val)

    def popFront(self) -> int:

        if len(self.queue) > 0:
            
            return self.queue.pop(0)
        else:

            return -1

    def popMiddle(self) -> int:
        if len(self.queue) > 0:

            middle_index = len(self.queue)//2 if len(self.queue) % 2 != 0 else (len(self.queue)//2)-1

            popped_val = self.queue[middle_index]

            del self.queue[middle_index]
            
            return popped_val

        else:
            return -1

    def popBack(self) -> int:

        if len(self.queue) > 0:

            popped_val = self.queue.pop(-1)
            
            return popped_val
        else:
            return -1


q = FrontMiddleBackQueue()
q.pushFront(1)
q.pushBack(2)
q.pushMiddle(3)
q.pushMiddle(4)
print(q.popFront())
print(q.popMiddle())
print(q.popMiddle())
print(q.popBack())
print(q.popFront())
