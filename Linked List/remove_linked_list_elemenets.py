# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head, val):

        previous = None
        current = head

        while current:

            if current.val == val:
                if not previous:
                    head = head.next
                    previous = None
                    current = current.next
                    continue
                else:
                    while current and current.val == val:
                        current = current.next

                    previous.next = current
                    previous = current
                    if current:
                        current = current.next
                    continue

            else:
                current = current.next
                if not previous:
                    previous = head
                else:
                    previous = previous.next

        return head


list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(2)
list1.next.next.next = ListNode(4)

list1.next.next.next.next = ListNode(5)
list1.next.next.next.next.next = ListNode(2)

# list1.next.next.next.next.next.next = ListNode(1)
# list1.next.next.next.next.next.next.next = ListNode(4)

sol = Solution()

print_linked_list(sol.removeElements(list1, 2))
