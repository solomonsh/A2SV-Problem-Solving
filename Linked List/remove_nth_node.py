# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def removeNthFromEnd(self, head, n):

        fast = head
        slow = None
        count = 1

        while fast:

            fast = fast.next
            count += 1

            if count >= n+1:
                if slow is None:
                    slow = head
                else:
                    slow = slow.next

            if fast is None or fast.next is None:
                if slow is None:
                    return head.next
                if slow.next:
                    slow.next = slow.next.next
                    return head
        return None


sol = Solution()

list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(3)
list1.next.next.next = ListNode(4)
list1.next.next.next.next = ListNode(5)


sol.removeNthFromEnd(list1, 2)
