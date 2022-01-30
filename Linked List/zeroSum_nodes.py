# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def remove_node(self, head, node1, node2):

        dummy = ListNode()
        dummy.next = head

        current = dummy

        while current.next:
            if current.next == node1:
                node1_current = node1

                if not node2:
                    current.next = current.next.next
                else:
                    while node1_current != node2:
                        node1_current = node1_current.next

                    current.next = node1_current.next

            else:
                current = current.next

        return dummy.next

    def removeZeroSumSublists(self, head):

        current1 = head

        while current1:

            sum_zero = current1.val

            current2 = current1.next

            if (sum_zero == 0 and current2 and current2.val != 0) or (sum_zero == 0 and not current2):

                head_removed = self.remove_node(head, current1, None)

                return self.removeZeroSumSublists(head_removed)

            while current2:
                sum_zero += current2.val
                if sum_zero == 0:

                    head_removed = self.remove_node(head, current1, current2)

                    return self.removeZeroSumSublists(head_removed)

                current2 = current2.next

            current1 = current1.next

        return head