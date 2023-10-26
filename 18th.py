class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_position(self, data, position):
        new_node = Node(data)
        
        if position == 1:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(1, position - 1):
                if current is None:
                    print("Position out of range.")
                    return
                current = current.next
            if current is None:
                print("Position out of range.")
                return
            new_node.next = current.next
            current.next = new_node

    def delete_at_position(self, position):
        if self.head is None:
            print("List is empty.")
            return None

        if position == 1:
            deleted_data = self.head.data
            self.head = self.head.next
            return deleted_data

        current = self.head
        for _ in range(1, position - 1):
            if current is None or current.next is None:
                print("Position out of range.")
                return
            current = current.next

        if current.next is None:
            print("Position out of range.")
            return

        deleted_data = current.next.data
        current.next = current.next.next
        return deleted_data

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


linked_list = LinkedList()

linked_list.insert_at_position(10, 1)
linked_list.insert_at_position(20, 2)
linked_list.insert_at_position(30, 2)

linked_list.display()
deleted_data = linked_list.delete_at_position(2)
if deleted_data is not None:
    print("Deleted node with data:", deleted_data)
else:
    print("Node not deleted or position out of range.")

linked_list.display()  