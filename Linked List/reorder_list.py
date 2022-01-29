# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
 
    def get_last_nodes(self,head):
        
        if head.next:
            iter = head.next
            slow = head

            while iter.next:
                    iter = iter.next
                    slow = slow.next

            return slow
        else:
            return head

    def get_without_last(self,head):
        
        if head.next:
            iter = head.next
            slow = head

            while iter.next:
                    iter = iter.next
                    slow = slow.next

            slow.next = None
            return head
        else:
            return head


    def reorderList(self, head):
        
        if not head.next:
            return head
        
        if not head.next.next:
            return head
        first_node = head 
        first_node_next = head.next

        last_node_prev = self.get_last_nodes(head)
        last_node = last_node_prev.next

 
        current = head
        while current:

            first_node.next = last_node
            without_last = self.get_without_last(first_node_next)
 
            last_node.next = without_last

            first_node = without_last
            first_node_next = first_node.next

            last_node_prev = self.get_last_nodes(first_node)
            last_node = last_node_prev.next

            if first_node == last_node_prev:
                return 
            
            current = current.next
 

        
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(3)
list1.next.next.next = ListNode(4)
list1.next.next.next.next = ListNode(5)
 


sol = Solution()

sol.reorderList(list1)