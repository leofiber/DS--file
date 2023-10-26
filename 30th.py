class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

    def pop(self):
        if not self.is_empty():
            popped_item = self.top.data
            self.top = self.top.next
            return popped_item
        else:
            print("Stack is empty.")
            return None

    def peek(self):
        if not self.is_empty():
            return self.top.data
        else:
            print("Stack is empty.")
            return None

    def size(self):
        current = self.top
        count = 0
        while current:
            count += 1
            current = current.next
        return count


stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print("Stack size:", stack.size())


print("Top element:", stack.peek())


popped_item = stack.pop()
print("Popped element:", popped_item)


print("Stack size after pop:", stack.size())

