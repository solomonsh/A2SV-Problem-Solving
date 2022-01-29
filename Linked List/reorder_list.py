# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def reverse_linkedList(self, head):

        previous = None
        current = head

        while current:

            next = current.next
            current.next = previous

            previous = current

            current = next

        return previous

    def reorderList(self, head):

        slow = fast = head
        prev_slow = None

        while fast and fast.next:
            prev_slow = slow
            slow = slow.next
            fast = fast.next.next

        middle = slow

        previous = break_point = self.reverse_linkedList(middle)
        prev_slow.next = previous

        dummy = dummy_curr = ListNode()
        current1 = head

        while break_point != current1:

            current1_next = current1.next
            dummy_curr.next = current1
            dummy_curr.next.next = previous

            dummy_curr = dummy_curr.next.next
            previous = previous.next
            current1 = current1_next

        return dummy.next


list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(3)
list1.next.next.next = ListNode(4)
list1.next.next.next.next = ListNode(5)


sol = Solution()


# print_linked_list(sol.reverse_linkedList(list1))
