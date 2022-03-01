class ListNode:
    def __init__(self, val):

        self.val = val
        self.next = None


class MyHashSet:

    def __init__(self):
        self.arraySize = 1000
        self.hashSetValues = [None for item in range(1000)]

    def add(self, key: int) -> None:
        if not self.contains(key):
            array_index = key % self.arraySize

            newNode = ListNode(key)

            if self.hashSetValues[array_index] == None:
                self.hashSetValues[array_index] = newNode

            else:
                current = self.hashSetValues[array_index]
                while current.next:

                    current = current.next

                current.next = newNode

    def remove(self, key: int) -> None:
        if self.contains(key):

            array_index = key % self.arraySize
            current = previous = self.hashSetValues[array_index]

            if not current:
                return

            if current.val == key:
                self.hashSetValues[array_index] = current.next

            else:

                current = current.next

                while current:
                    if current.val == key:
                        previous.next = current.next
                        break
                    else:
                        previous = previous.next
                        current = current.next

    def contains(self, key: int) -> bool:
        array_index = key % self.arraySize
        current = self.hashSetValues[array_index]

        while current:
            if current.val == key:
                return True
            else:
                current = current.next

        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
