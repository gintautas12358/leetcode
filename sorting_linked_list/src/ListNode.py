
from numpy import empty


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"{__class__.__name__} ({self.val}, {self.next})"
    
    def __eq__(self, other: object) -> bool:
        sameVal = self.val == other.val
        sameNext = self.next == other.next
        return sameVal and sameNext

def toListNode(l):
    if not l:
        return []
        
    head = ListNode(l[0])
    node = head
    for element in l[1:]:
        nn = ListNode(element)
        node.next = nn
        node = nn

    return head

def ln2List(ln):
    l = []
    while(ln):
        l.append(ln.val)
        ln = ln.next
    
    return l

if __name__ == "__main__":
    l = [1,2,3,4,5]
    print(toListNode(l))
    print(ln2List(toListNode(l)))

