
# Definition for a Node.
from sqlalchemy import true


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head):

        lists_dict = {}

        current = head
        while current:
            lists_dict[current] = Node(current.val)
            current = current.next

        newHead = Node(0)
        added = False
        for old, new in lists_dict.items():
            if not added:
                newHead.next = new
                added = true

            if old.next is None:
                new.next = None
            if old.random is None:
                new.random = None

            if old.next is not None:
                new.next = lists_dict[old.next]
            if old.random is not None:
                new.random = lists_dict[old.random]

        newHead = newHead.next
        return newHead

 

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
