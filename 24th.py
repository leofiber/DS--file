class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

doubly_linked_list = DoublyLinkedList()
doubly_linked_list.append(10)
doubly_linked_list.append(20)
doubly_linked_list.append(30)
doubly_linked_list.append(40)

print("Forward traversal:")
doubly_linked_list.display()  

