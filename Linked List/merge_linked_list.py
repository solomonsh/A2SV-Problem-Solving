# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def mergeTwoLists(self, list1, list2):

        current1, current2 = list1, list2

        if current1 is None:
            return current2
        if current2 is None:
            return current1

        if current1.val < current2.val:
            merged_list = ListNode(current1.val)
            current1 = current1.next
        else:
            merged_list = ListNode(current2.val)
            current2 = current2.next

        merged_list_counter = merged_list

        while current1 and current2:

            if current1.val <= current2.val:
                merged_list_counter.next = ListNode(current1.val)
                current1 = current1.next
                merged_list_counter = merged_list_counter.next

            else:
                merged_list_counter.next = ListNode(current2.val)
                current2 = current2.next
                merged_list_counter = merged_list_counter.next

        if current1:
            merged_list_counter.next = current1
        if current2:
            merged_list_counter.next = current2

        return merged_list


sol = Solution()

list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

sol.mergeTwoLists(list1, list2)
