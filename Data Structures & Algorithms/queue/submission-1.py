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
        first_node = self.head.next

        self.head.next = new_node
        new_node.prev = self.head
        new_node.next = first_node
        first_node.prev = new_node
        # firstnode = self.head.next
        # firstnode.prev = new_node 
        # new_node.next = firstnode
        # new_node.prev = self.head
        # self.head.next = new_node
    

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        else:
            last_node = self.tail.prev
            value = last_node.value
            prev_node = last_node.prev
            self.tail.prev = prev_node
            prev_node.next = self.tail
            

            return value

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        
        first_node = self.head.next
        value = first_node.value
        second_node = first_node.next

        self.head.next = second_node
        second_node.prev = self.head

        # second_node = self.head.next
        # second_node.prev = self.head
    
        return value

        
