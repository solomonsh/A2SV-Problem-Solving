# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sizOflinkedlist(self, linkedlist):
        current = linkedlist
        size = 0

        while current:
            size += 1
            current = current.next
        return size

    def splitListToParts(self, head, k):

        length = self.sizOflinkedlist(head)
        result = [None]*k
        current = head
        parts_size = length//k

        counter = 0

        remainder = length % k

        while current:
            count = 0
            new_node = curr = ListNode()

            num = 0 if remainder <= 0 else 1

            while count < parts_size+num and counter < k:
                curr.next = current
                current = current.next
                curr = curr.next
                count += 1

            curr.next = None

            if counter >= k:
                counter = 0
                break

            result[counter] = new_node.next

            counter += 1
            remainder -= 1

        return result


sol = Solution()

list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(3)
list1.next.next.next = ListNode(4)
list1.next.next.next.next = ListNode(5)
list1.next.next.next.next.next = ListNode(6)
list1.next.next.next.next.next.next = ListNode(7)
list1.next.next.next.next.next.next.next = ListNode(8)
list1.next.next.next.next.next.next.next.next = ListNode(9)
list1.next.next.next.next.next.next.next.next.next = ListNode(10)

print(sol.splitListToParts(list1, 10))
