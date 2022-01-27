# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head):
     
            
        fast = head
        slow = head
        while fast and fast.next:
            
            fast = fast.next.next
            slow = slow.next
            
            if fast == slow:
                return True
            
        return False



list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)


sol = Solution()

# sol.hasCycle(list2)