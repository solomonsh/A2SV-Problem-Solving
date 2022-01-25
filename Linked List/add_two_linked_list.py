# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0

        pointer1,pointer2 = l1,l2

        result_list = ListNode()
        current = result_list

        while pointer1 or pointer2:
            
            new_sum_val = 0
            
            if pointer1 and pointer2:
                sum_val = pointer1.val + pointer2.val + carry
            elif pointer1 is None and pointer2 is not None:
                sum_val = 0 + pointer2.val + carry
            elif pointer1 is not None and pointer2 is  None:
                sum_val = pointer1.val + 0 + carry

            if sum_val >= 10:
                new_sum_val = sum_val
                sum_val = sum_val%10
                carry = new_sum_val //10
            else:
                carry = 0
            
            current.next = ListNode(sum_val)
            current =  current.next
  
            pointer1 = pointer1.next if pointer1 else None
            pointer2 = pointer2.next if pointer2 else None
          
        if carry != 0 and new_sum_val >= 10:
            current.next = ListNode(carry)
        return result_list.next

sol = Solution()

# list1 = ListNode(9)
# list1.next = ListNode(9)
# list1.next.next = ListNode(9)
# list1.next.next.next = ListNode(9)
# list1.next.next.next.next = ListNode(9)
# list1.next.next.next.next.next = ListNode(9)
# list1.next.next.next.next.next.next = ListNode(9)

# list2 = ListNode(9)
# list2.next = ListNode(9)
# list2.next.next = ListNode(9)
# list2.next.next.next = ListNode(9)


list1 = ListNode(8)
list1.next = ListNode(3)
list1.next.next = ListNode(2)

list2 = ListNode(9)
list2.next = ListNode(2)
list2.next.next = ListNode(1)



sol.addTwoNumbers(list1, list2)


 