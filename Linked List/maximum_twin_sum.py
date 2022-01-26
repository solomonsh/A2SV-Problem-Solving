# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head):

        previous = None
        current = head

        while current:
            
            next_node = current.next

            current.next = previous

            previous = current

            current = next_node

        return previous

    def pairSum(self, head):

        current1 = head
        current2 = head
        inital = None

        max_sum = 0
        reversed = False

        while current1 or current2:

            if current1 is None or current1.next is None:
                if not reversed:
                    current2 = self.reverseList(current2)
                    reversed = True

                if inital is None:
                    inital = head

                temp_sum = inital.val + current2.val
                if temp_sum > max_sum:
                    max_sum = temp_sum
                inital = inital.next
                current2 = current2.next

            else:
                current1 = current1.next.next
                current2 = current2.next

        return max_sum


list2 = ListNode(47)
list2.next = ListNode(22)
list2.next.next = ListNode(81)
list2.next.next.next = ListNode(46)
list2.next.next.next.next = ListNode(94)
list2.next.next.next.next.next = ListNode(95)

sol = Solution()

sol.pairSum(list2)
