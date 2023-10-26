class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Queue is empty.")
            return None

    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            print("Queue is empty.")
            return None

    def size(self):
        return len(self.items)

queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Queue elements:", queue.items)


print("Queue size:", queue.size())


print("Front element:", queue.front())


dequeued_item = queue.dequeue()
print("Dequeued element:", dequeued_item)


print("Queue size after dequeue:", queue.size())

