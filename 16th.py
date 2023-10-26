class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_at_beginning(self):
        if self.head is not None:
            deleted_data = self.head.data
            self.head = self.head.next
            return deleted_data
        else:
            return None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


linked_list = LinkedList()
linked_list.insert_at_beginning(30)
linked_list.insert_at_beginning(20)
linked_list.insert_at_beginning(10)

linked_list.display() 

deleted_data = linked_list.delete_at_beginning()
if deleted_data is not None:
    print("Deleted node with data:", deleted_data)
else:
    print("List is empty.")

linked_list.display()  
