
def bubbleSort(head):

    if not head or not head.next:
        return head
    
    nn = head.next
    if head.val > nn.val:
        head.next = None
        nn.next = head
        head = nn

    return head