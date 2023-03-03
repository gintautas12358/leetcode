from .ListNode import ListNode

def sizeOfListNode(head):
    count = 0
    n = head
    while(n):
        count += 1
        n = n.next
    return count

def split(head):
    size = sizeOfListNode(head)
    mid = size/2

    count = 0
    n = head
    while(count < mid-1):
        count += 1
        n = n.next

    n2 = n.next
    n.next = None

    return head, n2

def smerge(n1, n2):
    
    if n1.val > n2.val:
        n2.next = n1
        return n2
    
    n1.next = n2
    return n1

def mergeSort(head):

    if not head or not head.next:
        return head
  
    n1, n2 = split(head)


    new_head = smerge(n1, n2)


    return new_head