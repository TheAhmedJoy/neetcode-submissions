class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:
    def __init__(self):
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        temp = self.head.next

        while temp and index > 0:
            temp = temp.next
            index -= 1
        
        if temp and temp != self.tail and index == 0:
            return temp.val

        return -1

    def addAtHead(self, val: int) -> None:
        temp_node = ListNode(val)
        next = self.head.next
        prev = self.head
        prev.next = temp_node
        next.prev = temp_node
        temp_node.prev = prev
        temp_node.next = next

    def addAtTail(self, val: int) -> None:
        temp_node = ListNode(val)
        prev = self.tail.prev
        next = self.tail
        prev.next = temp_node
        next.prev = temp_node
        temp_node.prev = prev
        temp_node.next = next

    def addAtIndex(self, index: int, val: int) -> None:
        temp = self.head.next

        while temp and index > 0:
            temp = temp.next
            index -= 1

        if temp and index == 0:
            temp_node = ListNode(val)
            next = temp
            prev = temp.prev
            prev.next = temp_node
            next.prev = temp_node            
            temp_node.prev = prev
            temp_node.next = next


    def deleteAtIndex(self, index: int) -> None:
        temp = self.head.next
        
        while temp and index > 0:
            temp = temp.next
            index -= 1
        
        if temp and temp != self.tail and index == 0:
            next = temp.next
            prev = temp.prev
            next.prev = prev
            prev.next = next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
