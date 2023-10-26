class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if not self.is_empty():
            item = self.front.data
            self.front = self.front.next
            return item
        else:
            print("Queue is empty.")
            return None

    def front_element(self):
        if not self.is_empty():
            return self.front.data
        else:
            print("Queue is empty.")
            return None

    def size(self):
        current = self.front
        count = 0
        while current:
            count += 1
            current = current.next
        return count


queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Queue size:", queue.size())


print("Front element:", queue.front_element())


dequeued_item = queue.dequeue()
print("Dequeued element:", dequeued_item)


print("Queue size after dequeue:", queue.size())

