import random
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:

    def __init__(self, head):
        self.head = head

    # Space complexity  N
    # Time complextiy N

    def getRandom(self) -> int:
        values_list = []

        current = self.head

        while current:
            values_list.append(current.val)

            current = current.next

        random_idx = random.randint(0, len(values_list)-1)
        return values_list[random_idx]

    def sizOflinkedlist(self, linkedlist):
        current = linkedlist
        size = 0

        while current:
            size += 1
            current = current.next
        return size

    # Space complexity  1
    # Time complextiy N

    def getRandom(self) -> int:
        current = self.head
        random_idx = random.randint(0, self.sizOflinkedlist(self.head)-1)

        count = 0
        while current:
            if count == random_idx:
                return current.val
            current = current.next
            count += 1
