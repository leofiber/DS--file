class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class CircularLinkedList:
    def __init__(self):
        self.head = None
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head  # Create a loop by pointing back to itself
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
    def display(self):
        if not self.head:
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break

circular_linked_list = CircularLinkedList()
circular_linked_list.append(10)
circular_linked_list.append(20)
circular_linked_list.append(30)
circular_linked_list.append(40)

circular_linked_list.display()
