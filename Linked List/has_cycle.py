def has_cycle(head):
    slow = fast = head
    
    while fast.next:
        if not fast.next.next:
            return 0
        fast = fast.next.next
        slow = slow.next
        
        if fast is slow:
            return 1
    
    return 0