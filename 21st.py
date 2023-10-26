class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def find_merge_point(head1, head2):
    def get_length(head):
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        return length

    len1 = get_length(head1)
    len2 = get_length(head2)

    current1 = head1
    current2 = head2
    if len1 > len2:
        for _ in range(len1 - len2):
            current1 = current1.next
    else:
        for _ in range(len2 - len1):
            current2 = current2.next

    while current1 != current2:
        current1 = current1.next
        current2 = current2.next

    return current1

list1 = Node(10)
list1.next = Node(20)
list1.next.next = Node(30)

list2 = Node(5)
list2.next = Node(25)
list2.next.next = list1.next.next  

merge_point = find_merge_point(list1, list2)

if merge_point:
    print("Merge point data:", merge_point.data)
else:
    print("No merge point found.")
