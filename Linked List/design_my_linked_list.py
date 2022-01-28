class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.head = None

    def addAtHead(self, val: int) -> None:

        new_node = ListNode(val)
        new_node.next = self.head

        self.head = new_node

    def get(self, index: int) -> int:

        count = 0
        current = self.head

        while current:
            if index == count:
                return current.val

            current = current.next
            count += 1

        return -1

    def addAtTail(self, val: int) -> None:

        if not self.head:
            self.addAtHead(val)

        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = ListNode(val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
        else:
            previous = None
            current = self.head
            i = 0

            while current and i < index:
                previous = current
                current = current.next
                i += 1

            if current and previous:
                previous.next = ListNode(val, current)

            if not current and previous:
                self.addAtTail(val)

    def deleteAtIndex(self, index: int) -> None:
        if self.head:
            if index == 0:

                self.head = self.head.next

            else:
                count = 1
                previous = self.head
                if self.head:
                    current = self.head.next
                else:
                    current = self.head
                while current:

                    if index == count:
                        previous.next = current.next
                        break
                    current = current.next
                    previous = previous.next
                    count += 1
