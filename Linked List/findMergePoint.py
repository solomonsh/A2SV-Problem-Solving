
def lengthOfLinkedList(head):
    count = 0
    current = head

    while current:
        count += 1
        current = current.next

    return count

def findMergeNode(head1, head2):
    
    current1 = head1
    current2 = head2 
   
    length_head1 = lengthOfLinkedList(head1)
    length_head2 = lengthOfLinkedList(head2)

    length_difference1 = length_head1-length_head2
    length_difference2 = length_head2-length_head1


    if length_difference1>0:
        while length_difference1 >0:
            current1 = current1.next
            length_difference1 -=1

    elif length_difference2>0:
        while length_difference2 >0:
            current2 = current2.next
            length_difference2 -=1

    

  
    
    while current1 and current2:
        if current1 == current2:
            return current1.val
        
        current1 = current1.next
        current2 = current2.next