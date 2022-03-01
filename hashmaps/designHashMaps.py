class ListNode:
    def __init__(self, key, val):

        self.pair = (key, val)
        self.next = None


class MyHashMap:

    def __init__(self):

        self.array_size = 1000
        self.array = [None for item in range(1000)]

    def hash(self, key):
        key = str(key)
        key_bytes = key.encode()
        hash_code = sum(key_bytes)

        return hash_code

    def compressor(self, hash_code):

        return hash_code % self.array_size

    def put(self, key: int, value: int) -> None:

        array_index = self.compressor(self.hash(key))
       

        newNode = ListNode(key, value)

        if self.array[array_index] == None:
            self.array[array_index] = newNode

        else:
            current = self.array[array_index]
            while True:
                # key is the same, update value
                if current.pair[0] == key:
                    current.pair = (key, value)
                    return
                if current.next == None:
                    break
                current = current.next

            current.next = ListNode(key, value)

    def get(self, key: int) -> int:
        array_index = self.compressor(self.hash(key))
        current = self.array[array_index]

        while current:
            if current.pair[0] == key:
                return current.pair[1]
            else:
                current = current.next

        return -1

    def remove(self, key: int):

        array_index = self.compressor(self.hash(key))
        current = previous = self.array[array_index]

        if not current:
            return

        if current.pair[0] == key:
            self.array[array_index] = current.next

        else:

            current = current.next

            while current:
                if current.pair[0] == key:
                    previous.next = current.next
                    break
                else:
                    previous = previous.next
                    current = current.next



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
