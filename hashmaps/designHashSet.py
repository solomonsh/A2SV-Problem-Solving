class MyHashSet:

    def __init__(self):
        self.hashSetValues = []

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.hashSetValues.append(key)
        
        

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.hashSetValues.remove(key)
        

    def contains(self, key: int) -> bool:
        return key in self.hashSetValues
        



