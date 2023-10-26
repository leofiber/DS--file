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

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

def merge_sorted_lists(list1, list2):
    merged_list = LinkedList()
    current1 = list1.head
    current2 = list2.head

    while current1 and current2:
        if current1.data < current2.data:
            merged_list.append(current1.data)
            current1 = current1.next
        else:
            merged_list.append(current2.data)
            current2 = current2.next

    while current1:
        merged_list.append(current1.data)
        current1 = current1.next

    while current2:
        merged_list.append(current2.data)
        current2 = current2.next

    return merged_list


list1 = LinkedList()
list2 = LinkedList()

#appending elements in ll1
list1.append(5)
list1.append(15)
list1.append(25)

#appending elemets in ll2
list2.append(10)
list2.append(20)
list2.append(30)

list1.display()  
list2.display()  

merged_list = merge_sorted_lists(list1, list2)

print("\nMerged sorted list:")
merged_list.display() 
