class MyCircularDeque:

    def __init__(self, k: int):
        self.size = 0
        self.deque = []
        self.maxSize = k
        
    def insertFront(self, value: int) -> bool:
        if not self.isFull():
            self.deque.insert(0,value)
            self.size += 1
            return True
        
        else:
            return False

    def insertLast(self, value: int) -> bool:
        
          if not self.isFull():
            self.deque.append(value)
            self.size += 1
            return True
        
          else:
            return False

    def deleteFront(self) -> bool:
        
         if not self.isEmpty():
            self.deque.pop(0)
            self.size -= 1
            return True
        
         else:
            return False
        
        

    def deleteLast(self) -> bool:
        
        if not self.isEmpty():
            self.deque.pop()
            self.size -= 1
            return True
        
        else:
            return False
        

    def getFront(self) -> int:
        
        if not self.isEmpty():
            return self.deque[0]
        
        else:
            return -1
        

    def getRear(self) -> int:
         
        if not self.isEmpty():
            return self.deque[-1]
        
        else:
            return -1

    def isEmpty(self) -> bool:
        
        if self.size == 0: return True
        else : return False
        

    def isFull(self) -> bool:
        if self.size  == self.maxSize: return True
        else : return False
        