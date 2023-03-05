
from .ListNode import toListNode, ln2List, ListNode

# 1 complexity
def popNode(head):
    nn = head.next
    n = head
    n.next = None
    return n, nn

# 1 complexity
def append(head, n):
    if head is None:
        head = n
    else: 
        head.next = n
    return n

def appendAll(result_last, head):
    while head is not None:
        n, head = popNode(head)
        result_last = append(result_last, n)

def popSmallerFront(left, right):
    if left.val > right.val:
        n, right = popNode(right)
    else:
        n, left = popNode(left)

    return n, left, right

def merge(left, right):
    result_last = None
    result = None
    while left is not None and right is not None:
        n, left, right = popSmallerFront(left, right)

        result_last = append(result_last, n)
        if result is None:
            result = result_last

    appendAll(result_last, left)
    appendAll(result_last, right)

    return result

def getNode(head, nth):
    count = 0
    n = head
    while(count < nth-1):
        n = n.next 
        count += 1

    return n

def mergeSort(head, size):
    if (size <= 1):
        return head
    
    mid = int(size/2)
    n = getNode(head, mid)
    
    _, right = popNode(n)
    left = head

    left = mergeSort(left, mid)
    right = mergeSort(right, size-mid)
    return merge(left, right)
