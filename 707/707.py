class ListNode():
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:
    def __init__(self):
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index: int) -> int:
        current = self.left.next
        while current and index > 0:
            current = current.next
            index -= 1
        
        if index == 0 and current != self.right and current:
            return current.val
        return -1
        
    def addAtHead(self, val: int) -> None:
        prev, new_node, next = self.left, ListNode(val), self.left.next
        prev.next = new_node
        new_node.prev = prev
        new_node.next = next
        next.prev = new_node
        
    def addAtTail(self, val: int) -> None:
        prev, new_node, next = self.right.prev, ListNode(val), self.right
        prev.next = new_node
        new_node.prev = prev
        new_node.next = next
        next.prev = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        current = self.left.next
        while current and index > 0:
            index -= 1
            current = current.next
        
        if current and index == 0:
            prev, new_node = current.prev, ListNode(val)
            prev.next = new_node
            new_node.prev = prev
            new_node.next = current
            current.prev = new_node

    def deleteAtIndex(self, index: int) -> None:
        current = self.left.next
        while current and index > 0:
            index -= 1
            current = current.next

        if current and index == 0 and current != self.right:
            prev, next = current.prev, current.next
            prev.next = next
            next.prev = prev
