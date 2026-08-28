class Node:
    def __init__(self,value):
        self.value = value
        self.prev = None
        self.next = None
        
class Deque:
   
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        new_node = Node(value)
        lastnode = self.tail.prev
        lastnode.next = new_node
        new_node.prev = lastnode
        new_node.next = self.tail
        self.tail.prev = new_node
        
    def appendleft(self, value: int) -> None:
        new_node = Node(value)
        firstnode = self.head.next
        firstnode = new_node.next 
        new_node.prev = self.head
        self.head.next = new_node
        new_node.next = firstnode

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        else:
            lastnode = self.tail.prev
            prevnode = lastnode.prev
            value = lastnode.value
            prevnode.next = self.tail
            self.tail.prev = prevnode

            return value

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        
        firstnode = self.head.next
        value = firstnode.value
        secondnode = firstnode.next
        secondnode = self.head.next
        secondnode.prev = self.head
    
        return value

        
