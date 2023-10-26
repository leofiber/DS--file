class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def search(self, target):
        current = self.head
        position = 1
        while current:
            if current.data == target:
                return position
            current = current.next
            position += 1
        return -1

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

linked_list = LinkedList()

linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
linked_list.append(40)
linked_list.append(50)

linked_list.display()  

target = 30
position = linked_list.search(target)
if position != -1:
    print(f"{target} found at position {position}.")
else:
    print(f"{target} not found in the list.")
