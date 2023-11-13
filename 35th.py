def is_operator(char):
    return char in "+-*/"

def precedence(operator):
    if operator in "*/":
        return 2
    elif operator in "+-":
        return 1
    else:
        return 0

def infix_to_postfix(expression):
    stack = []
    postfix = []
    
    for char in expression:
        if char.isalnum():
            postfix.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != '(' and precedence(char) <= precedence(stack[-1]):
                postfix.append(stack.pop())
            stack.append(char)
    
    while stack:
        postfix.append(stack.pop())
    
    return ''.join(postfix)

def infix_to_prefix(expression):
    expression = expression[::-1]
    expression = expression.replace('(', 'temp').replace(')', '(').replace('temp', ')')
    postfix = infix_to_postfix(expression)
    prefix = postfix[::-1]
    
    return prefix

infix_expression = "a+b*(c-d)"
print("Infix Expression:", infix_expression)

prefix_expression = infix_to_prefix(infix_expression)
print("Prefix Expression:", prefix_expression)
