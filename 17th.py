class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete_at_end(self):
        if self.head is None:
            return None
        elif self.head.next is None:
            deleted_data = self.head.data
            self.head = None
        else:
            current = self.head
            while current.next.next:
                current = current.next
            deleted_data = current.next.data
            current.next = None
        return deleted_data

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


linked_list = LinkedList()
linked_list.insert_at_end(10)
linked_list.insert_at_end(20)
linked_list.insert_at_end(30)

linked_list.display()  
deleted_data = linked_list.delete_at_end()
if deleted_data is not None:
    print("Deleted node with data:", deleted_data)
else:
    print("List is empty.")

linked_list.display() 
