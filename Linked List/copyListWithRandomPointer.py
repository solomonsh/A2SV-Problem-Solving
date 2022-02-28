
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head):

        copyList = Node(0)
        copyCurrent = copyList

        currentOld = head

        randomPointer = {}
        values = {}

        count = 0
        while currentOld:

            values[currentOld] = count
            currentOld = currentOld.next
            count += 1

        currentOld = head

        while currentOld:

            if currentOld.random is not None:
                randomPointer[currentOld] = values[currentOld.random]

            else:
                randomPointer[currentOld] = None

            copyCurrent.next = Node(currentOld.val)

            currentOld = currentOld.next
            copyCurrent = copyCurrent.next

        copyList = copyList.next
        copyCurrent = copyList
        currentOld = head

        while currentOld:

            if currentOld.random is None:
                copyCurrent.random = None
            else:
                count = 0
                temp_current = copyList
                while count < randomPointer[currentOld]:
                    temp_current = temp_current.next
                    count += 1

                copyCurrent.random = temp_current

            copyCurrent = copyCurrent.next
            currentOld = currentOld.next

        return copyList


head = Node(7)
head.next = Node(13)
head.next.next = Node(11)
head.next.next.next = Node(10)
head.next.next.next.next = Node(1)

head.random = None
head.next.random = head
head.next.next.random = head.next.next.next.next
head.next.next.next.random = head.next.next
head.next.next.next.next.random = head


def printLinkedList(head):
    current = head
    while current:
        print(current.val)
        current = current.next


sol = Solution()

printLinkedList(sol.copyRandomList(head))
