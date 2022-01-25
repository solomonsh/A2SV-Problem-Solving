# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head):
        current = head

        while current and current.next:
            next_node = current.next
            if current.val == next_node.val:
                current.next = next_node.next
            else:
                current = current.next

        return head


sol = Solution()

list1 = ListNode(1)
list1.next = ListNode(1)
list1.next.next = ListNode(2)
list1.next.next.next = ListNode(3)
list1.next.next.next.next = ListNode(3)
sol.deleteDuplicates(list1)
