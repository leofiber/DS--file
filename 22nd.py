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
    def has_cycle(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True 
        return False  
    def remove_cycle(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        if fast is None or fast.next is None:
            return

        slow = self.head
        while slow.next != fast.next:
            slow = slow.next
            fast = fast.next

        fast.next = None

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
linked_list.head.next.next.next.next.next = linked_list.head.next 
if linked_list.has_cycle():
    print("Cycle detected.")
    linked_list.remove_cycle()
    print("Cycle removed.")
else:
    print("No cycle detected.")

linked_list.display() 
