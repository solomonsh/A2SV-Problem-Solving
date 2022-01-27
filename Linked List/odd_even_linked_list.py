# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head):

        if head is None: return None

        current1  = head # odd
        current2 = head.next # even
        
    
        evens_list_current = current2
      
        while current2 and current2.next:

            current1.next = current2.next
            current1 = current1.next

            current2.next = current1.next
            current2 = current2.next
        

        current1.next = evens_list_current

        return head
            
     



 
sol = Solution()

list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(3)
list1.next.next.next = ListNode(4)
list1.next.next.next.next = ListNode(5)


sol.oddEvenList(list1)
