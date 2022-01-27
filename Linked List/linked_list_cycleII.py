# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head):
        nexts = set()

        current = head

        count = 0
        while current:
            if current.next not in nexts:
                nexts.add(current)
            else:
                return current.next

            current = current.next

        return None
