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

    def find_nth_from_end(self, n):
        if not self.head or n <= 0:
            return None

        first_ptr = self.head
        second_ptr = self.head

        
        for _ in range(n):
            if first_ptr is None:
                return None
            first_ptr = first_ptr.next

   
        while first_ptr:
            first_ptr = first_ptr.next
            second_ptr = second_ptr.next

        return second_ptr.data

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage:
linked_list = LinkedList()


linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
linked_list.append(40)
linked_list.append(50)

linked_list.display() 

n = 3 
nth_node = linked_list.find_nth_from_end(n)

if nth_node is not None:
    print(f"The {n}th node from the end is: {nth_node}")
else:
    print("Invalid input or N is out of range.")
