# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def printLinkedList(self, head):
        current = head

        while current:
            print(current.val)
            current = current.next

    def mergeTwoLists(self, list1, list2):

        result = current3 = ListNode()

        while list1 and list2:

            if list1.val <= list2.val:
                current3.next = list1
                list1 = list1.next

            else:
                current3.next = list2
                list2 = list2.next

            current3 = current3.next

        current3.next = list1 or list2

        return result.next


sol = Solution()

list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

sol.printLinkedList(sol.mergeTwoLists(list1, list2))
