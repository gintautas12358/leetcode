
from .ListNode import toListNode, ln2List, ListNode

# 1 complexity
def popFront(head):
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

def merge(left, right):
    result_last = None
    result = result_last
    n = None
    while left is not None and right is not None:

        if left.val > right.val:
            n, right = popFront(right)
        else:
            n, left = popFront(left)

        result_last = append(result_last, n)
        if result is None:
            result = result_last
         
    while left is not None:

        n, left = popFront(left)
        result_last = append(result_last, n)

    while right is not None:
        n, right = popFront(right)
        result_last = append(result_last, n)

    return result

def mergeSort(head, size):
    if (size <= 1):
        return head
    
    mid = int(size/2)

    count = 0
    n = head
    while(count < mid-1):
        n = n.next 
        count += 1

    right = n.next
    n.next = None
    left = head

    left = mergeSort(left, mid)
    right = mergeSort(right, size-mid)
    return merge(left, right)

if __name__ == "__main__":   
    a = [2,1,5,4]
    al = toListNode(a)
    sal = mergeSort(al)
    print("out", sal)