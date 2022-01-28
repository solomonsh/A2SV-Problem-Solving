import random
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head):
        self.head = head
        

    def getRandom(self) -> int:
        values_list = []
        
        current = self.head
        
        while current:
            values_list.append(current.val)
             
            current = current.next
        
        random_idx = random.randint(0,len(values_list)-1)
        return values_list[random_idx]
        

