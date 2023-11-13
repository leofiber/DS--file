class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, x: int):
        if not self.stack:
            self.stack.append((x, x))
        else:
            current_min = self.stack[-1][1]
            self.stack.append((x, min(x, current_min)))

    def pop(self):
        if self.stack:
            self.stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1][0]

    def getMin(self):
        if self.stack:
            return self.stack[-1][1]

min_stack = MinStack()

while True:
    element = input("Enter an element to push (or 'q' to quit): ")
    if element.lower() == 'q':
        break

    try:
        element = int(element)
        min_stack.push(element)
        print(f"{element} has been pushed into the stack.")
    except ValueError:
        print("Please enter a valid integer or 'q' to quit.")

top_element = min_stack.top()
print("Top Element:", top_element)

min_element = min_stack.getMin()
print("Minimum Element:", min_element)

min_stack.pop()

new_top_element = min_stack.top()
print("New Top Element:", new_top_element)
