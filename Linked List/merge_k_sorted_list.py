# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists):

        if len(lists) == 1:
            return lists[0]

        if len(lists) == 0:
            return None

        if len(lists) == 2:
            sorted_list = current = ListNode()
            list1 = lists[0]
            list2 = lists[1]

            while list1 and list2:

                if list1.val <= list2.val:
                    current.next = list1
                    list1 = list1.next
                else:
                    current.next = list2
                    list2 = list2.next

                current = current.next

            if list1:
                current.next = list1
            if list2:
                current.next = list2

            return sorted_list.next
        else:
            k = len(lists)
            lists_ = [self.mergeKLists(
                lists[0:(k//2)+1]), self.mergeKLists(lists[(k//2)+1:k])]

            return self.mergeKLists(lists_)


def print_linked_list(head):
    current = head

    while current:
        print(current.val)
        current = current.next


list1 = ListNode(1)
list1.next = ListNode(4)
list1.next.next = ListNode(5)


list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

list3 = ListNode(2)
list3.next = ListNode(6)

lists = [list1, list2, list3]

sol = Solution()

print_linked_list(sol.mergeKLists(lists))
