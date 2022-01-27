# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    
    def swapPairs(self, head):
        current = head
        previous = None
        
        if not head: return None
        if head.next:
            second_node = head.next
        else:
            return head

        previous_counter = 0
        while current and current.next:

            previous_counter +=1

            next_second_node = second_node.next
            second_node.next = current
            current.next = next_second_node
            
            if previous_counter == 1:
                previous = second_node

            if previous_counter>=2:
                cur = previous
                if previous_counter>2 : previous_counter+=1
                for _ in range(1,previous_counter):
                    cur = cur.next
                cur.next = second_node
                     
            if next_second_node and next_second_node.next:
                second_node = next_second_node.next

            current = current.next 

            
        return previous
     

            
       



sol = Solution()

list2 = ListNode(1)
list2.next = ListNode(2)
list2.next.next = ListNode(3)
list2.next.next.next = ListNode(4)
# list2.next.next.next.next = ListNode(5)
# list2.next.next.next.next.next = ListNode(6)
# list2.next.next.next.next.next.next = ListNode(7)
# list2.next.next.next.next.next.next.next = ListNode(8)

sol.swapPairs(list2)
