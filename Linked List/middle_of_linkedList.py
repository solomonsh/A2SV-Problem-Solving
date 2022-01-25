# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head):

        fast = head
        slow = head

        while fast:
            if fast.next is None:
                 break
            else:
             fast = fast.next.next
             slow = slow.next

        return slow
        