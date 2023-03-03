
def bubbleSort(head):

    if not head or not head.next:
        return head

    isSorted = False
    while(not isSorted):
        isSorted = True
        n = head
        while(n.next):
            nn = n.next
            if n.val > nn.val:
                isSorted = False
                n.val, nn.val = nn.val, n.val
                
            n = nn
        if isSorted:
            break

    return head