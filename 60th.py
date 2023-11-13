class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def evaluate_expression_tree(root):
    if root is not None:
        left_value = evaluate_expression_tree(root.left)
        right_value = evaluate_expression_tree(root.right)

        if root.val == '+':
            return left_value + right_value
        elif root.val == '-':
            return left_value - right_value
        elif root.val == '*':
            return left_value * right_value
        elif root.val == '/':
            return left_value / right_value

    return int(root.val)

def build_expression_tree(tokens):
    stack = []
    for token in tokens:
        node = TreeNode(token)
        if token in "+-*/":
            node.right = stack.pop()
            node.left = stack.pop()
        stack.append(node)
    return stack[0]

expression = input("Enter the expression in postfix notation ").split()

expression_tree = build_expression_tree(expression)

result = evaluate_expression_tree(expression_tree)
print(f"Result of the expression tree: {result}")
