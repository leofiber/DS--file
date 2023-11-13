class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

def get_height(node):
    if not node:
        return 0
    return node.height

def get_balance_factor(node):
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)

def rotate_left(y):
    x = y.right
    T2 = x.left

    x.left = y
    y.right = T2

    y.height = 1 + max(get_height(y.left), get_height(y.right))
    x.height = 1 + max(get_height(x.left), get_height(x.right))

    return x

def rotate_right(x):
    y = x.left
    T2 = y.right

    y.right = x
    x.left = T2

    x.height = 1 + max(get_height(x.left), get_height(x.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))

    return y

def insert(root, key):
    if not root:
        return AVLNode(key)

    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    root.height = 1 + max(get_height(root.left), get_height(root.right))

    balance = get_balance_factor(root)

    if balance > 1:
        if key < root.left.key:
            return rotate_right(root)
        else:
            root.left = rotate_left(root.left)
            return rotate_right(root)

    if balance < -1:
        if key > root.right.key:
            return rotate_left(root)
        else:
            root.right = rotate_right(root.right)
            return rotate_left(root)

    return root

def print_avl(root, level=0, prefix="Root: "):
    if root is not None:
        print(" " * (level * 2) + prefix + str(root.key))
        if root.left is not None or root.right is not None:
            print_avl(root.left, level + 1, "L--> ")
            print_avl(root.right, level + 1, "R--> ")

root = None
keys = [10, 20, 30, 40, 50, 25]
for key in keys:
    root = insert(root, key)

print("AVL Tree:")
print_avl(root)
