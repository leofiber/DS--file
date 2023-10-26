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

    def is_palindrome(self):
        def reverse_linked_list(head):
            prev = None
            current = head
            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev

        if not self.head:
            return True  

        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_half = slow
        first_half = self.head

       
        second_half = reverse_linked_list(second_half)

        
        while second_half:
            if first_half.data != second_half.data:
                return False
            first_half = first_half.next
            second_half = second_half.next

        return True

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

linked_list = LinkedList()


linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(2)
linked_list.append(1)

linked_list.display()  

is_palindrome = linked_list.is_palindrome()
if is_palindrome:
    print("The linked list is a palindrome.")
else:
    print("The linked list is not a palindrome.")
