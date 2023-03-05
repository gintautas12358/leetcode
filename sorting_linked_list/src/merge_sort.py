
from .ListNode import toListNode, ln2List, ListNode

def sizeOfListNode(head):
    count = 0
    n = head
    while(n):
        count += 1
        n = n.next
    return count

def lastListNode(head):
    n = head
    while(n.next):
        n = n.next
    return n

def merge(left, right):
    n = left
    while(n.next):
        n = n.next

    n.next = right
    return left

def popFront(head):
    nn = head.next
    n = head
    n.next = None
    return n, nn

def append(head, n):
    if head is None:
        head = n
    else: 
        lastListNode(head).next = n

    return head

def nmerge(left, right):
    # print(left, right)
    result = None
    n = None
    while sizeOfListNode(left) > 0 and sizeOfListNode(right) > 0:
        if left.val > right.val:
            n, right = popFront(right)
        else:
            n, left = popFront(left)

        result = append(result, n)
        # print("loop append", result)
        
        

    while sizeOfListNode(left) > 0:
        n, left = popFront(left)
        result = append(result, n)
        # print("append", result)

    while sizeOfListNode(right) > 0:
        n, right = popFront(right)
        result = append(result, n)
        # print("append", result)

    
        

    return result

def mergeSort(head, size):
    # print(size, head)

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


    return nmerge(left, right)

if __name__ == "__main__":   
    a = [2,1,5,4]
    al = toListNode(a)
    sal = mergeSort(al)
    print("out", sal)