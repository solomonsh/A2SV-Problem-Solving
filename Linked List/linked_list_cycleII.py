# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    # Approach 1
    # Time complexity n
    # Space complexity n

    def detectCycle(self, head):
        nexts = set()

        current = head

 
        while current:
            if current.next not in nexts:
                nexts.add(current)
            else:
                return current.next

            current = current.next

        return None



    # Approach 2
    # Time complexity n
    # Space complexity 1
    
    def detectCycle(self, head):

        fast = head
        slow = head
    
        while fast and fast.next:
             
            fast = fast.next.next
            slow = slow.next
            
            if fast == slow:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
         