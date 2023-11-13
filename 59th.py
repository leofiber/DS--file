class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
        self.height = 1

def get_height(node):
    if node is None:
        return 0
    return node.height

def get_balance_factor(node):
    if node is None:
        return 0
    return get_height(node.left) - get_height(node.right)

def update_height(node):
    if node is not None:
        node.height = 1 + max(get_height(node.left), get_height(node.right))

def right_rotate(y):
    x = y.left
    T2 = x.right

    x.right = y
    y.left = T2

    update_height(y)
    update_height(x)

    return x

def left_rotate(x):
    y = x.right
    T2 = y.left

    y.left = x
    x.right = T2

    update_height(x)
    update_height(y)

    return y

def balance(node, value):
    balance_factor = get_balance_factor(node)

    if balance_factor > 1 and value < node.left.val:
        return right_rotate(node)
    if balance_factor < -1 and value > node.right.val:
        return left_rotate(node)
    if balance_factor > 1 and value > node.left.val:
        node.left = left_rotate(node.left)
        return right_rotate(node)
    if balance_factor < -1 and value < node.right.val:
        node.right = right_rotate(node.right)
        return left_rotate(node)

    return node

def insert(root, value):
    if root is None:
        return TreeNode(value)

    if value < root.val:
        root.left = insert(root.left, value)
    elif value > root.val:
        root.right = insert(root.right, value)
    else:
        return root

    update_height(root)

    return balance(root, value)

def get_min_value_node(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def delete_node(root, value):
    if root is None:
        return root

    if value < root.val:
        root.left = delete_node(root.left, value)
    elif value > root.val:
        root.right = delete_node(root.right, value)
    else:
        if root.left is None or root.right is None:
            temp = root.left if root.left else root.right
            if temp is None:
                temp = root
                root = None
            else:
                root = temp
            del temp
        else:
            temp = get_min_value_node(root.right)
            root.val = temp.val
            root.right = delete_node(root.right, temp.val)

    if root is None:
        return root

    update_height(root)

    return balance(root, value)

def inorder_traversal(root):
    if root is None:
        return
    inorder_traversal(root.left)
    print(root.val, end=" ")
    inorder_traversal(root.right)

root = None

root = insert(root, 10)
root = insert(root, 20)
root = insert(root, 30)
root = insert(root, 40)
root = insert(root, 50)
root = insert(root, 25)

print("Before deletion:")
inorder_traversal(root)
print()

root = delete_node(root, 30)

print("After deletion:")
inorder_traversal(root)
print()
