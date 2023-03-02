
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"{__class__.__name__} ({self.val}, {self.next})"

def toListNode(l):
    
    head = ListNode()
    node = head
    for element in l:
        nn = ListNode(element)
        node.next = nn
        node = nn

    return head

if __name__ == "__main__":
    l = [1,2,3,4,5]
    print(toListNode(l))