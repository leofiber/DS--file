class QueueUsingStacks:
    def __init__(self):
        self.stack_enq = []
        self.stack_deq = []

    def is_empty(self):
        return not self.stack_enq and not self.stack_deq

    def enqueue(self, item):
        self.stack_enq.append(item)

    def dequeue(self):
        if not self.stack_deq:
            if not self.stack_enq:
                return None
            while self.stack_enq:
                self.stack_deq.append(self.stack_enq.pop())
        item = self.stack_deq.pop()
        
        while self.stack_deq:
            self.stack_enq.append(self.stack_deq.pop())
            
        return item

queue = QueueUsingStacks()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Queue after enqueue(1):", queue.stack_enq, "=>", queue.stack_deq)
print("Queue after enqueue(2):", queue.stack_enq, "=>", queue.stack_deq)
print("Queue after enqueue(3):", queue.stack_enq, "=>", queue.stack_deq)

print("Dequeue result (1st time):", queue.dequeue())
print("Queue after dequeue(1):", queue.stack_enq, "=>", queue.stack_deq)

print("Dequeue result (2nd time):", queue.dequeue())
print("Queue after dequeue(2):", queue.stack_enq, "=>", queue.stack_deq)

queue.enqueue(4)
print("Queue after enqueue(4):", queue.stack_enq, "=>", queue.stack_deq)

print("Dequeue result (3rd time):", queue.dequeue())
print("Queue after dequeue(3):", queue.stack_enq, "=>", queue.stack_deq)

print("Dequeue result (4th time):", queue.dequeue())
print("Queue after dequeue(4):", queue.stack_enq, "=>", queue.stack_deq)
